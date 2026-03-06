from analyzer import analyze_log


def test_analyze_log_counts(tmp_path):
    log_content = "\n".join(
        [
            "INFO: Start",
            "FAIL: A",
            "WARNING: W1",
            "ERROR: E1",
            "FAIL: B",
            "INFO: End",
        ]
    )

    log_file = tmp_path / "test.log"
    log_file.write_text(log_content, encoding="utf-8")

    report = analyze_log(str(log_file))

    assert report["fail_count"] == 2
    assert report["error_count"] == 1
    assert report["warning_count"] == 1
    assert report["total_errors"] == 3
    assert len(report["errors"]) == 3
