import os
import MudekParser as mp
import time
import psutil


# ----------------- MAIN EXECUTION BLOCK -------------------
for x in os.listdir('outputs/'):
    print(f"Deleting {x} from output folder...")
    os.remove(os.path.join('outputs/', x))

# st = time.time()
# print("CPU USAGE BEFORE: ", psutil.cpu_percent())
mp.assemble_report_file()
# print("CPU USAGE AFTER: ", psutil.cpu_percent())
# et = time.time()
# elapsed_time = et - st
# print("Execution time: ", elapsed_time, ' seconds')

# print(mp.list_students_above_3_avg())
#
# print(mp.list_all_sub_outcomes_under_3_avg_by_students())
#
# print(mp.min_of_all_sub_outcomes_by_lectures())
#
# print(mp.avg_of_all_sub_outcomes_by_lectures())
#
# print(mp.list_all_lectures_under_3_avg())
