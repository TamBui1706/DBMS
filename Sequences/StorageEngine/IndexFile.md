# Sequence Diagrams: IndexFile

## 🆕 Added Properties & Methods for `IndexFile`
To support the detailed sequence logic for unit testing, the following missing properties/methods have been introduced. **Please update the `IndexFile` class in your Class Diagram with these:**

- **Property** added to `IndexFile`: `fileStream` (IO stream handle)

---

This file contains the detailed sequence diagrams for all unit tests of the **IndexFile** class in the Storage Engine subsystem.

## 1. Init_OpensFileStreamForIndexBlocks

```mermaid
sequenceDiagram
    actor Test
    participant IndexFile

    Test->>IndexFile: new IndexFile(path)
    IndexFile->>IndexFile: open fileStream(path, 'rb+')
    IndexFile-->>Test: return instance
```

## 2. WriteBlock_SavesBytesToDisk

```mermaid
sequenceDiagram
    actor Test
    participant IndexFile

    Test->>IndexFile: writeBlock(blockId, data)
    IndexFile->>IndexFile: fileStream.seek(offset)
    IndexFile->>IndexFile: fileStream.write(data)
    IndexFile-->>Test: success
```

