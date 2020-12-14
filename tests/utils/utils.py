import mock


def mock_response(
    status: int = 200,
    content: str = "CONTENT",
    json_data: dict = None,
    raise_for_status: Exception = None,
):
    mock_resp = mock.Mock()
    mock_resp.raise_for_status = mock.Mock()
    if raise_for_status:
        mock_resp.raise_for_status.side_effect = raise_for_status

    mock_resp.status_code = status
    mock_resp.content = content
    if json_data:
        mock_resp.json = mock.Mock(return_value=json_data)
    return mock_resp
