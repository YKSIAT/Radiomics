# -*- coding: utf-8 -*-
import os
import xlwt


root_path = "E:\\PLG\\PLG_66"

workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('sheet1', cell_overwrite_ok=True)

sub_dirs = [x[0] for x in os.walk(root_path)]
is_root_dir = True

adc_path_list = []
flair_path_list = []
t1c_path_list = []
t2wi_path_list = []
t1wi_path_list = []
patients = []
for index, sub_dir in enumerate(sub_dirs):
    # print("sub_dir is ", sub_dir)
    if is_root_dir:
        is_root_dir = False
        continue
    num_name_list = []

    if os.path.basename(sub_dir) != "label_nii":
        patients.append(sub_dir)

        # print("sub_dir", sub_dir)
        # print(sub_dir.split("\\")[-1].strip())
        num_name_list.append(sub_dir.split("\\")[-1].strip())

        label_model_name = []
        image_model_name = []
        final_label_name_list = []
        files_list = os.listdir(sub_dir)
        # print("files_list", len(files_list))
        for item in files_list:
            # print(item)
            if item.split(".")[-1].strip() == "mat":
                items = item.split(".")[-2].strip() + ".nii"
                label_nii_path = os.path.join(sub_dir, "label_nii", items)
                # print("label_nii_path", label_nii_path)
                label_model_name.append(label_nii_path)
            if item.split(".")[-1].strip() == "nii":
                # print("item HAH", item)
                image_model_name.append(item)
                image_nii_path = os.path.join(sub_dir, item)
        if len(label_model_name) == 10:
            for item in label_model_name:
                if ("EDEMA" in item.split("\\")[-1].strip().split("_")
                        or "edma" in item.split("\\")[-1].strip().split("_")):
                    final_label_name_list.append(item)
        else:
            final_label_name_list = label_model_name

        for item in image_model_name:
            # print("hah", item)
            # print(item.split("_")[-1].split(".")[0])
            model = item.split("_")[-1].strip().split(".")[0].strip()
            model_nii = model + ".nii"

            for item1 in final_label_name_list:
                # print("item1", item1)

                if model in item1.split("\\")[-1].strip().split("_") \
                        or model_nii in item1.split("\\")[-1].strip().split("_"):
                    image_nii_path_new = os.path.join(root_path, sub_dir, item)
                    # print("label_model_name", item1)

                    if model == "ADC":
                        adc_path_list.append(item1)

                    elif model == "FLAIR":
                        flair_path_list.append(item1)
                        # print("********************")
                        # print(item1)
                    elif model == "T1C":
                        t1c_path_list.append(item1)
                        # print(item1)
                    elif model == "T2WI":
                        t2wi_path_list.append(item1)
                        # print(item1)
                    else:
                        t1wi_path_list.append(item1)
                        print("********************")
        # print("image_model_name", len(image_model_name))
        print(len(label_model_name), len(image_model_name))
        print()
        print()

# print(len(patients))

print(len(adc_path_list))
print(len(flair_path_list))
print(len(t1c_path_list))
print(len(t2wi_path_list))
print(len(t1wi_path_list))
# print(adc_path_list)

image_models = ["reg_ADC.nii", "reg_FLAIR.nii", "reg_T1C.nii", "reg_T2WI.nii", "T1WI.nii"]
for index, value in enumerate(adc_path_list):
    print(value.split("\\label_nii")[0])
    for i in range(len(image_models)):
        print(os.path.join(value.split("\\label_nii")[0], image_models[i]))
        worksheet.write(index, i, os.path.join(value.split("\\label_nii")[0], image_models[i]))

workbook.save('./Excel_all_image_model_list_66.xls')
# for index, value in enumerate(patients):
#     worksheet.write(index, 0, value.split("\\")[-1])
#     worksheet.write(index, 1, adc_path_list[index])
#     worksheet.write(index, 2, flair_path_list[index])
#     worksheet.write(index, 3, t1c_path_list[index])
#     worksheet.write(index, 4, t2wi_path_list[index])
#     worksheet.write(index, 5, t1wi_path_list[index])
#
# workbook.save('./Excel_all_model_list_66.xls')











