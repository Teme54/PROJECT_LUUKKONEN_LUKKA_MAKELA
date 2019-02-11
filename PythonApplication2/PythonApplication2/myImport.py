class job():

    job_count = 0

    def __init__(self, job_name):
        print ("Calling job constructor")
        job.job_count += 1
        self.job_name = job_name

    def __del__(self):
        print (self, "MyClass object destroyed")

    def show_job(self):
        print("My job is " + self.job_name + " and job count is", job.job_count)
        