# -*- conding: urf-8 -*-
import csv

def save_to_file(jobs):
    file = open("coupon.csv", mode="w", newline='')
    writer = csv.writer(file)
    writer.writerow(["name", "price", "status"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return 