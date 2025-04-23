import time
# logic for otp based approach
wait_time=1
attempt =0 
max_retries =5

while attempt <=max_retries:
    print(f"Attempt : {attempt+1} -  Wait Time : {wait_time}")
    time.sleep(wait_time)
    attempt+=1
    wait_time*=2  #doubling wait time
    continue