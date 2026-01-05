import json
class LogAnalyze:
    def __init__(self, file_name, file_output):
        self.file_name = file_name
        self.file_output = file_output

    def read_log(self):
        with open(self.file_name, "r") as file:
            return file.readlines()
    def add_json(self,count):
        with open(self.file_output, "w+") as file_json:
            json.dump(count, file_json, indent=4)
    def log_analyze(self):
        log_count = {
            "INFO": 0,
            "WARNING":0,
            "ERROR":0
        }
        lines = self.read_log()
        for line in lines:
            if "INFO" in line:
                log_count.update({"INFO": log_count["INFO"] +1})
            elif "WARNING" in line:
                log_count.update({"WARNING": log_count["WARNING"] +1})
            elif "ERROR" in line:
                log_count.update({"ERROR": log_count["ERROR"] +1})
            else:
                pass
        self.add_json(log_count)
    #------------------------------------ output in txt file------------------
    # def add_txt(count):
    #     with open("log.txt", "w+") as file_log:
    #         for key, value in count.items():
    #             file_log.writelines(f"{key}: {value}\n" )

            
log_01 = LogAnalyze("app_log.py", "output_error.json")
log_count = log_01.log_analyze()