class Response:
    def __init__(self, status_code, message, data=None):
        self.status_code = status_code
        self.message = message
        self.data = data

    def to_dict(self):
        response = {
            'status_code': self.status_code,
            'message': self.message,
        }
        if self.data is not None:
            response['data'] = self.data
        return response
    
def response_success(message, data=None):
    return Response(200, message, data).to_dict()

def response_error(message, data=None):
    return Response(500, message, data).to_dict()

# Example usage
if __name__ == "__main__":
    success_response = Response(200, "Request successful", {"key": "value"})
    print(success_response.to_dict())

    error_response = Response(404, "Resource not found")
    print(error_response.to_dict())