import os
import tensorflow as tf
import numpy


dir_path = "~/Downloads/i-LIDS-VID/sequences"

def get_file(dir_path):
    persons = []
    labels = []

    for cam in os.listdir(dir_path):
        for person in cam:
            for eachimageofoneperson in person:
                labels.append(int(eachimageofoneperson[11:14]))
                persons.append(eachimageofoneperson)
    return persons,labels