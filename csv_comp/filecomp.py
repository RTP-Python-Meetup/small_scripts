import csv

# Open files to compare
file1= open('ct.csv', newline='')
f1lines=tuple(csv.reader(file1))

file2=open('ft.csv', newline='')
f2lines=tuple(csv.reader(file2))

# Get the headers of each file stripped of whitespaces
f1headers = tuple(item.strip() for item in f1lines[0])
f2headers = tuple(item.strip() for item in f2lines[0])

# Get the indicies of columns we're checking
mp_col = f1headers.index('Mapping_Product')
ms_col = f1headers.index('Mapping_Segment')
rs_col = f1headers.index('Report_Section')
actuals_col = f1headers.index('Actuals')

mrdcd_col = f2headers.index('MBR_RPT_DETL_CAT_DESC')
mc_col = f2headers.index('member_count')

for f1line in f1lines[1:]:
    if all(i=='' for i in f1line):
        continue
    for f2line in f2lines[1:]:
        f1_mp = f1line[mp_col].strip()
        f1_ms = f1line[ms_col].strip()
        f1_rs = f1line[rs_col].strip()
        actuals = int(f1line[actuals_col])

        f2_mrdcd = f2line[mrdcd_col]
        mc = int(f2line[mc_col])
        if f1_mp in f2_mrdcd and f1_rs in f2_mrdcd and f1_rs in f2_mrdcd:
            if actuals == mc:
                print("Match                 : ", end='')
            else:
                print("Fail {:>8}/{:<8}: ".format(actuals, mc), end='')
            print("{}, {}, {} - {}".format(f1_mp, f1_ms, f1_rs, f2_mrdcd))
