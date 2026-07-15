# Detailed Guide: 9 Business Flows - Concrete Examples & Line-by-Line Code Explanation

This document explains each business flow of the **DBMS Index Management (B+ Tree)** system following a 3-part structure:
1. **Concrete example with specific numbers** (for easy visualization).
2. **Actual Python code snippets** (extracted from `src/`).
3. **Detailed line-by-line code explanation** (to deeply understand the core).

---

## 1. FLOW 1: POINT SEARCH

### 1.1 Concrete Example with Numbers
We want to search for key **`35`** on a 2-level high B+ Tree:
*   **Root Page (ID = 1):** Contains routing key `[50]`, pointing to the left child page `ID = 2` (where keys < 50 reside) and the right child page `ID = 3` (where keys >= 50 reside).
*   **Left Leaf Page (ID = 2):** Contains data pairs `[(10, RecordID(1,10)), (30, RecordID(1,30)), (35, RecordID(1,35))]`.

**Execution Process:**
1.  System checks the index state (e.g., `VALID`).
2.  Starts from Root (`ID = 1`). Acquires read latch on Root.
3.  Compares search key `35` with routing key `50`. Since `35 < 50`, the system decides to go down to left child page `ID = 2`.
4.  Acquires read latch on child page `ID = 2`, releases read latch on Root `ID = 1`.
5.  On leaf page `ID = 2`, binary searches and finds key `35` matching the record with address `RecordID(page_id=1, slot_id=35)`.
6.  Returns the result and releases latch on page `ID = 2`.

---

### 1.2 Corresponding Python Code Snippet
```python
def point_search(self, key: Any) -> List[RecordID]:
    if self._metadata.state != IndexState.VALID:
        raise IndexUnusableException("Index is corrupted or not ready")
        
    leaf = self._engine.search(self._metadata.root_page_id, key)
    rids = leaf.lookup(key, self._engine._key_comparator)
    self._engine._concurrency_manager.release_all_latches()
    return rids
```

---

### 1.3 Line-by-Line Source Code Explanation
*   `def point_search(self, key: Any) -> List[RecordID]:`
    *   *Explanation:* Defines the point search function receiving a `key` (e.g., `35`) and returning a list of `RecordID` record addresses.
*   `if self._metadata.state != IndexState.VALID:`
    *   *Explanation:* Checks the state of the index. The index must be in a valid (`VALID`) state to be allowed to query data.
*   `raise IndexUnusableException("Index is corrupted or not ready")`
    *   *Explanation:* If the index is in an `INVALID` or `UNUSABLE` state, raises an exception to notify the Client.
*   `leaf = self._engine.search(self._metadata.root_page_id, key)`
    *   *Explanation:* Calls the Engine tool to perform tree traversal downwards from the root (`self._metadata.root_page_id`) to find the leaf page object `leaf` containing the search `key`.
*   `rids = leaf.lookup(key, self._engine._key_comparator)`
    *   *Explanation:* Performs a direct search on the leaf page's record list using the key comparator `self._engine._key_comparator` to extract the `rids` address array.
*   `self._engine._concurrency_manager.release_all_latches()`
    *   *Explanation:* Releases all read latches held on pages during the search so other threads can access them.
*   `return rids`
    *   *Explanation:* Returns the list of found record addresses to the user.

---

## 2. FLOW 2: RANGE SCAN

### 2.1 Concrete Example with Numbers
We want to find all records with keys in the range **`[15, 35]`** (forward scan):
*   **Leaf Page 1 (ID = 2):** Contains keys `[10, 20]`. Its next leaf page is `next_page_id = 4`.
*   **Leaf Page 2 (ID = 4):** Contains keys `[30, 40]`.

**Execution Process:**
1.  Engine finds the leaf page containing the first key satisfying `>= 15`. This is Leaf Page 1 (`ID = 2`).
2.  Read latches Leaf Page 1. The Iterator (`RangeIterator`) is initialized at Leaf Page 1, pointing the traversal pointer to the element containing key `20` (because key `10 < 15` is ignored).
3.  Returns key `20` to the user. Traversal pointer increments by 1 (running out of elements on Leaf Page 1).
4.  To continue reading, the iterator acquires a read latch on the next leaf page `ID = 4` (`next_page_id`), releasing the latch on Leaf Page 1.
5.  The iterator continues to read key `30` on Leaf Page 2 and returns the result.
6.  The next key on Leaf Page 2 is `40`. Since `40 > 35` (exceeding scan boundary), the iterator halts and releases the latch on Leaf Page 2.

---

### 2.2 Corresponding Python Code Snippet
```python
def __next__(self) -> IndexEntry:
    while self._current_leaf:
        entries = self._current_leaf.entries
        if self._direction == ScanDirection.FORWARD:
            if self._current_idx < len(entries):
                entry = entries[self._current_idx]
                self._current_idx += 1
                if self._comparator.compare(entry.key, self._end_key) > 0:
                    raise StopIteration()
                if not entry.is_deleted:
                    return entry
            else:
                next_id = self._current_leaf.next_page_id
                if next_id == -1:
                    raise StopIteration()
                sibling = self._page_directory[next_id]
                self._concurrency.acquire_latch(sibling, LatchMode.READ)
                self._concurrency.release_latch(self._current_leaf)
                self._current_leaf = sibling
                self._current_idx = 0
    raise StopIteration()
```

---

### 2.3 Line-by-Line Source Code Explanation
*   `def __next__(self) -> IndexEntry:`
    *   *Explanation:* The function to get the next element of a Python Iterator. It will return a valid `IndexEntry` every time it's called.
*   `while self._current_leaf:`
    *   *Explanation:* Loop continuously as long as the current leaf page exists.
*   `entries = self._current_leaf.entries`
    *   *Explanation:* Retrieves the list of all physically stored records on the current leaf page.
*   `if self._direction == ScanDirection.FORWARD:`
    *   *Explanation:* Checks if the scan direction is forward (ascending keys).
*   `if self._current_idx < len(entries):`
    *   *Explanation:* If the current traversal pointer index is still less than the total number of records in this leaf page.
*   `entry = entries[self._current_idx]`
    *   *Explanation:* Retrieves the record at the current pointer position.
*   `self._current_idx += 1`
    *   *Explanation:* Increments the traversal pointer index by 1 in preparation for the next call.
*   `if self._comparator.compare(entry.key, self._end_key) > 0:`
    *   *Explanation:* Compares the current record's key with the upper limit `self._end_key`. If greater, it means we have finished scanning the requested range.
*   `raise StopIteration()`
    *   *Explanation:* Throws a StopIteration error to signal Python to stop the range traversal loop.
*   `if not entry.is_deleted:`
    *   *Explanation:* Checks if the record is marked as logically deleted.
*   `return entry`
    *   *Explanation:* Returns the valid record to the user.
*   `else:` (Line 13 - Out of elements on the current leaf page)
    *   *Explanation:* This branch runs when it has traversed all elements on the current leaf page but has not exceeded the upper limit.
*   `next_id = self._current_leaf.next_page_id`
    *   *Explanation:* Gets the address of the next sibling leaf page via the horizontal link pointer.
*   `if next_id == -1:`
    *   *Explanation:* If there are no more sibling pages (this is the rightmost page).
*   `raise StopIteration()`
    *   *Explanation:* Ends the iteration process.
*   `sibling = self._page_directory[next_id]`
    *   *Explanation:* Retrieves the sibling leaf page object from the page directory.
*   `self._concurrency.acquire_latch(sibling, LatchMode.READ)`
    *   *Explanation:* Acquires a `READ` read latch on the new sibling leaf page to ensure thread-safe reading.
*   `self._concurrency.release_latch(self._current_leaf)`
    *   *Explanation:* Releases the read latch on the old leaf page.
*   `self._current_leaf = sibling`
    *   *Explanation:* Switches the current leaf page to the new sibling page to continue the data scanning loop.
*   `self._current_idx = 0`
    *   *Explanation:* Resets the traversal pointer index to the first position of the new page.

---

## 3. FLOW 3: INSERT & SPLIT

### 3.1 Concrete Example with Numbers
A leaf page can hold a maximum of **`2`** keys (`max_capacity = 2`). Currently, leaf page `ID = 5` holds keys `[10, 20]`. We perform inserting key **`30`**:
1.  Temporarily insert key `30` into the page, the key count increases to 3 `[10, 20, 30]`.
2.  System detects overflow: `3 > max_capacity` (3 > 2).
3.  Allocates a new leaf page `ID = 6`.
4.  Splits data in half:
    *   Old leaf page `ID = 5` keeps the left part: `[10]`.
    *   New leaf page `ID = 6` receives the remaining elements: `[20, 30]`.
5.  Updates horizontal links: `leaf_5.next_page_id = 6`, `leaf_6.prev_page_id = 5`.
6.  Pushes the smallest key of the new page, which is `20`, up to the routing parent page.

---

### 3.2 Corresponding Python Code Snippet
```python
def split(self) -> Tuple[Any, BTreeNode]:
    sibling = LeafNode(-1, NodeHeader(level=self.header.level))
    mid = len(self.entries) // 2
    median_key = self.entries[mid].key

    sibling.entries = self.entries[mid:]
    self.entries = self.entries[:mid]

    self.keys = [e.key for e in self.entries]
    self.record_ids = [e.rid for e in self.entries]
    self.header.key_count = len(self.keys)

    sibling.keys = [e.key for e in sibling.entries]
    sibling.record_ids = [e.rid for e in sibling.entries]
    sibling.header.key_count = len(sibling.keys)

    return median_key, sibling
```

---

### 3.3 Line-by-Line Source Code Explanation
*   `def split(self) -> Tuple[Any, BTreeNode]:`
    *   *Explanation:* The leaf node split method returns a tuple comprising: Separating key (`median_key`) and the new sibling page object (`sibling`).
*   `sibling = LeafNode(-1, NodeHeader(level=self.header.level))`
    *   *Explanation:* Initializes a new sibling leaf page object with the same `level` as the current page.
*   `mid = len(self.entries) // 2`
    *   *Explanation:* Finds the median position of the record list to split the leaf page in half.
*   `median_key = self.entries[mid].key`
    *   *Explanation:* Retrieves the key value of the median record to act as the separating key pushed up to the parent page.
*   `sibling.entries = self.entries[mid:]`
    *   *Explanation:* Moves the latter half of the record list (from position `mid` to the end) to the new sibling leaf page.
*   `self.entries = self.entries[:mid]`
    *   *Explanation:* Trims off the latter half, keeping only the first half of the record list for the old leaf page.
*   `self.keys = [e.key for e in self.entries]`
    *   *Explanation:* Updates the key list (`keys`) for the old leaf page after it has been reduced.
*   `self.record_ids = [e.rid for e in self.entries]`
    *   *Explanation:* Updates the corresponding RecordID array for the old page.
*   `self.header.key_count = len(self.keys)`
    *   *Explanation:* Synchronizes the key count recorded in the old page's header.
*   `sibling.keys = [e.key for e in sibling.entries]`
    *   *Explanation:* Initializes the key list for the new sibling leaf page.
*   `sibling.record_ids = [e.rid for e in sibling.entries]`
    *   *Explanation:* Initializes the RecordID array for the new page.
*   `sibling.header.key_count = len(sibling.keys)`
    *   *Explanation:* Updates the key count in the new leaf page's header.
*   `return median_key, sibling`
    *   *Explanation:* Returns the separating key and the new sibling leaf page to the Engine for processing insertion onto the parent page.

---

## 5. FLOW 5: OPTIMISTIC READ

### 5.1 Concrete Example with Numbers
We want to quickly read which child page of internal page `ID = 2` (currently having `version = 5` written on the door) contains key `30`:
1.  **Check version beforehand:** You arrive at page `ID = 2`'s door, noting the version number is `v_start = 5`.
2.  **Read data:** You look up and see that key `30` points to child page `ID = 10`.
3.  **Check version afterwards:** You look back at the version number on the door:
    *   *Scenario 5A (No Conflict):* The version number is still `v_end = 5`. You confidently proceed down to child page `ID = 10` without queuing for a read latch.
    *   *Scenario 5B (Conflict Occurred):* The version number was changed to `v_end = 6` (because an insert thread just split this page). You know the result for child page `10` might be wrong. You immediately request a physical `READ` read latch on page `ID = 2` to re-read the accurate information.

---

### 5.2 Corresponding Python Code Snippet
```python
def search_optimistic(self, root_page_id: int, key: Any) -> int:
    node = self.pages[root_page_id]
    initial_version = node.header.version
    
    if isinstance(node, InternalNode):
        child_id = node.lookup(key, self._key_comparator)
    else:
        child_id = node.page_id
        
    final_version = node.header.version
    if initial_version != final_version:
        self._concurrency_manager.acquire_latch(node, LatchMode.READ)
        if isinstance(node, InternalNode):
            child_id = node.lookup(key, self._key_comparator)
        self._concurrency_manager.release_latch(node)
        
    return child_id
```

---

### 5.3 Line-by-Line Source Code Explanation
*   `def search_optimistic(self, root_page_id: int, key: Any) -> int:`
    *   *Explanation:* The optimistic read method receiving the starting page and the key to find, returning the child page's ID.
*   `node = self.pages[root_page_id]`
    *   *Explanation:* Retrieves the page object in memory.
*   `initial_version = node.header.version`
    *   *Explanation:* Quickly reads and stores the initial version number of the page (`version`) without acquiring a read latch.
*   `if isinstance(node, InternalNode):`
    *   *Explanation:* Checks whether the node is an internal node containing routing keys.
*   `child_id = node.lookup(key, self._key_comparator)`
    *   *Explanation:* Binary lookup to find the ID of the child page corresponding to the key.
*   `else:`
    *   *Explanation:* If the node is a leaf page (no child pages).
*   `child_id = node.page_id`
    *   *Explanation:* The child page is exactly the current page.
*   `final_version = node.header.version`
    *   *Explanation:* Reads the page's version number after having copied the directive data.
*   `if initial_version != final_version:`
    *   *Explanation:* Compares the version numbers before and after. If they differ, it proves the page was concurrently modified by another thread.
*   `self._concurrency_manager.acquire_latch(node, LatchMode.READ)`
    *   *Explanation:* Initiates the fallback mechanism: acquires a physical `READ` read latch on the page to block writers.
*   `if isinstance(node, InternalNode):`
    *   *Explanation:* Performs the routing lookup over from scratch.
*   `child_id = node.lookup(key, self._key_comparator)`
    *   *Explanation:* Retrieves the safe child page ID.
*   `self._concurrency_manager.release_latch(node)`
    *   *Explanation:* Releases the physical read latch after having finished re-reading.
*   `return child_id`
    *   *Explanation:* Returns the correct child page ID to the Engine.

---

## 7. FLOW 7: VACUUM MAINTENANCE (VACUUM & COMPACTION)

### 7.1 Concrete Example with Numbers
Leaf page `ID = 5` is containing 3 elements: `[(10, rid1), (20, rid2, is_deleted=True), (30, rid3)]`. Key `20` was previously logically deleted by the user, hence tagged `is_deleted=True`:
1.  The `IndexVacuumWorker` cleaner scans through leaf page `ID = 5`.
2.  Detects that the 2nd element (`key=20`) has the `is_deleted=True` flag.
3.  Completely removes this element from the page's physical array. The leaf page now only contains `[10, 30]`.
4.  Calls the page compression function `compress_nodes()` to free up empty bytes, updating `free_space` to gain an extra 100 bytes ready to receive new data.

---

### 7.2 Corresponding Python Code Snippet
```python
def vacuum(self, index_id: int) -> int:
    reclaimed = 0
    for page in list(self._engine.pages.values()):
        if isinstance(page, LeafNode):
            original_len = len(page.entries)
            page.entries = [e for e in page.entries if not e.is_deleted]
            page.keys = [e.key for e in page.entries]
            page.header.key_count = len(page.keys)
            reclaimed += (original_len - len(page.entries))
            self.compress_nodes(page)
    return reclaimed
```

---

### 7.3 Line-by-Line Source Code Explanation
*   `def vacuum(self, index_id: int) -> int:`
    *   *Explanation:* Defines the vacuum cleanup method for the index, returning the total number of records physically cleaned.
*   `reclaimed = 0`
    *   *Explanation:* Counter variable for the number of records whose memory space has been reclaimed.
*   `for page in list(self._engine.pages.values()):`
    *   *Explanation:* Iterates through all index pages currently held in the Engine.
*   `if isinstance(page, LeafNode):`
    *   *Explanation:* Only performs cleanup sweeping on leaf pages (where actual record data is stored).
*   `original_len = len(page.entries)`
    *   *Explanation:* Records the initial record count of the page (including logically deleted records).
*   `page.entries = [e for e in page.entries if not e.is_deleted]`
    *   *Explanation:* Uses list comprehension to filter and retain valid records, completely removing records with the `is_deleted == True` flag from the page's physical memory.
*   `page.keys = [e.key for e in page.entries]`
    *   *Explanation:* Updates the leaf page's key list corresponding to the remaining records.
*   `page.header.key_count = len(page.keys)`
    *   *Explanation:* Re-records the actual key count in the page header.
*   `reclaimed += (original_len - len(page.entries))`
    *   *Explanation:* Accumulates the number of records that were physically cleaned up from the page into the total counter.
*   `self.compress_nodes(page)`
    *   *Explanation:* Calls the prefix compression function to free up additional empty memory space for that leaf page.
*   `return reclaimed`
    *   *Explanation:* Returns the total number of records reclaimed for the system.

---

## 9. ADMINISTRATIVE UTILITIES (CREATE, DROP, UPDATE)

### 9.1 Concrete Example with Numbers
*   **Create Index:** The system initializes a new index named `"idx_customer_age"`. It automatically calls the Engine to create the first leaf page `ID = 1`, sets the tree height `tree_height = 1` and registers the normal operating index state `VALID`.
*   **Drop Index:** When an index is dropped, the system doesn't wipe the file clean right away but immediately changes its state to `UNUSABLE`. Any read/write thread calling the index from this second onwards is blocked and throws an error.
*   **Update Key:** A customer changes age from `25` to `26`. The index calls `delete(25)` to mark the old key as deleted, then calls `insert(26)` to insert the new key into the correct ascending index position.

---

### 9.2 Corresponding Python Code Snippet
```python
# Extracted from src/lifecycle_manager.py
def create_index(self, metadata: IndexMetadata) -> bool:
    leaf = self._engine.allocate_leaf()
    metadata.root_page_id = leaf.page_id
    metadata.state = IndexState.VALID
    metadata.tree_height = 1
    metadata.node_count = 1
    self._metadata_directory[metadata.index_id] = metadata
    return True

# Extracted from src/access_methods.py
def update(self, old_key: Any, new_key: Any, rid: RecordID) -> bool:
    self.delete(old_key, rid)
    return self.insert(new_key, rid)
```

---

### 9.3 Line-by-Line Source Code Explanation
#### A. `create_index` function:
*   `def create_index(self, metadata: IndexMetadata) -> bool:`
    *   *Explanation:* Index initialization method receiving the `metadata` object.
*   `leaf = self._engine.allocate_leaf()`
    *   *Explanation:* Requests the Engine to allocate the first physical page of the index tree as a leaf page.
*   `metadata.root_page_id = leaf.page_id`
    *   *Explanation:* Sets the root page ID of the index to be exactly the newly allocated leaf page ID.
*   `metadata.state = IndexState.VALID`
    *   *Explanation:* Activates the index state, turning it into `VALID` (allowing read/write queries).
*   `metadata.tree_height = 1`
    *   *Explanation:* Sets the initial index tree height to 1.
*   `metadata.node_count = 1`
    *   *Explanation:* Initializes the tree's current node count to 1.
*   `self._metadata_directory[metadata.index_id] = metadata`
    *   *Explanation:* Registers this index metadata into the centralized directory.
*   `return True`
    *   *Explanation:* Reports successful index initialization.

#### B. `update` function:
*   `def update(self, old_key: Any, new_key: Any, rid: RecordID) -> bool:`
    *   *Explanation:* The key value update method receiving the old key, new key, and record address.
*   `self.delete(old_key, rid)`
    *   *Explanation:* Calls the delete method to logically delete the old key value from the index tree.
*   `return self.insert(new_key, rid)`
    *   *Explanation:* Performs insertion of the new key along with the RecordID address into the correct distributed position on the B+ Tree and returns the success/failure result.
