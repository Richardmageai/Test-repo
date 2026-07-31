# QA Conflict Test Data

Branch: qa-conflict-manual-20260731

Use these files to manually test Mage and external IDE conflict handling.

Do not put real credentials in this repository. `qa_unrelated_keep.txt` is only a dummy file used to prove unrelated files are not changed.

## Files

- `qa_non_overlap_mage.txt`: edit only in Mage for the non-overlap test.
- `qa_non_overlap_external.txt`: edit only in the external IDE clone for the non-overlap test.
- `qa_overlap.txt`: edit in both Mage and the external IDE clone for the overlap conflict test.
- `qa_stale_editor.txt`: open in Mage, then edit in the external IDE clone before saving in Mage.
- `qa_dirty_pull.txt`: edit in Mage and externally, then test pull with dirty files.
- `qa_push_guard.txt`: commit in Mage while the external IDE clone has already pushed a newer commit.
- `qa_final_sync.txt`: use to test abort, retry, conflict markers, resolution, and final synchronization.
- `qa_unrelated_keep.txt`: do not edit; verify it stays unchanged.
