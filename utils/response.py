class Response:
    def common_response(data, status_code):
        return {
            "data": data,
            "status_code": status_code
        }

    def common_error_response(message, status_code=500, error=True):
        return {
            "message": message,
            "status_code": status_code,
            "error": error
        }