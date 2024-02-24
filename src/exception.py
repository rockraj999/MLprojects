import sys
## creating custom exception function

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()  ## exc_info will provide exc_tb where we can get 
                                        ## filename, line numner and what error  we are having in the code.
    file_name=exc_tb.tb_frame.f_code.co_filename

    error_message="error occured in python script name [{0}] in line number [{1}] error message is [{2}]".format(file_name,exc_tb.lineno,str(error))

    return error_message


## creating our own exception class inheriting from parent class "Exception" . and calling error_message_detail
## function to get granularity of error.
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super.__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message

