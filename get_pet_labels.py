#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Heba Fathy
# DATE CREATED:    22-06-2023                       
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    ## Imports only listdir function from OS module 
    ## Retrieve the filenames from folder pet_images/
    img_files = listdir(image_dir)
    # Dictionary with 'key' as image filename and 'value' as a List
    results_dic = dict()
    
    for i in range(0, len(img_files), 1):
         #pet labels to be lowercase
         if img_files[i][0] != ".":
            word_list_pet_image = img_files[i].lower().split("_")
            pet_name = ""
            for x in word_list_pet_image:
                if x.isalpha():
                   pet_name += x + " "
            #Stripping any whitespace characters from labels
            pet_name = pet_name.strip()     
            # Add only new image filename to the dictionary 
            if img_files[i] not in results_dic:
                results_dic[img_files[i]] = [pet_name]
            else:
                print("This image file already exist in the directory:", img_files[i])
         ## Prints resulting pet_name
         #print("\nFilename=", img_files[i], "   Label=", pet_name)
    return results_dic