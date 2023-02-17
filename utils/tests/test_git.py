import io
from unittest import mock

from utils import git


@mock.patch.object(git.os, "popen")
def test_get_latest_branches(mock_popen):
    mock_popen.return_value = io.StringIO(
        """0f35afc61fc HEAD@{2023-02-17 11:35:31 +0000}: checkout: moving from branchy-zero to branchy-one
00c6b379c8c HEAD@{2023-02-17 11:01:03 +0000}: checkout: moving from branchy-two to branchy-zero
021a871d1f1 HEAD@{2023-02-16 17:18:12 +0000}: checkout: moving from main to branchy-two
021a871d1f1 HEAD@{2023-02-16 17:15:51 +0000}: checkout: moving from branchy-three to main
021a871d1f1 HEAD@{2023-02-16 16:45:56 +0000}: checkout: moving from main to branchy-three
0c602a917f7 HEAD@{2023-02-16 16:08:37 +0000}: checkout: moving from branchy-four to main
0c602a917f7 HEAD@{2023-02-16 14:52:06 +0000}: checkout: moving from main to branchy-four
0c602a917f7 HEAD@{2023-02-16 14:51:49 +0000}: checkout: moving from branchy-five to main
0c602a917f7 HEAD@{2023-02-16 14:35:09 +0000}: checkout: moving from main to branchy-five
0c602a917f7 HEAD@{2023-02-16 13:54:29 +0000}: checkout: moving from branchy-six to main"""
    )

    branches = git.get_last_branches()

    assert len(branches) == 7
    assert branches == [
        "2023-02-17 11:35:31: branchy-one",
        "2023-02-17 11:01:03: branchy-zero",
        "2023-02-16 17:18:12: branchy-two",
        "2023-02-16 17:15:51: main",
        "2023-02-16 16:45:56: branchy-three",
        "2023-02-16 14:52:06: branchy-four",
        "2023-02-16 14:35:09: branchy-five",
    ]
