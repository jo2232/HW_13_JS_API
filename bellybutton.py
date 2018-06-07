import os
import csv
import pandas as pd
import json
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

def samples():
    samples = os.path.join('data', 'samples_data.csv')
    sample_df = pd.read_csv(samples)
    column_headers = list(sample_df)
    sample_names = column_headers[1:]

    samples_dict = {"sample_names": sample_names}

    def saveOutput(data):
            with open('sample_names.txt', 'w') as outfile:
                json.dump(data, outfile, sort_keys = True, indent = 2)

    saveOutput(sample_names)
    return (sample_names)

def otuList():
    otu = os.path.join('data', 'belly_button_biodiversity_otu_id.csv')
    otu_df = pd.read_csv(otu)
    taxo_unit = []
    for unit in otu_df["lowest_taxonomic_unit_found"]:
        taxo_unit.append(unit)
    otu_dict = {"lowest_taxonomic_unit_found": taxo_unit}

    def saveOutput(data):
            with open('bellybutton_taxo_otu.txt', 'w') as outfile:
                json.dump(data, outfile, sort_keys = True, indent = 2)

    saveOutput(otu_dict)
    return (otu_dict)

def meta(sampleName):
    metadata = os.path.join('data', 'Belly_Button_Biodiversity_Metadata.csv')
    metadata_df = pd.read_csv(metadata)
    sample_list = sampleName.split('_')
    sampleID = int(sample_list[1])
    metadata_list = []
    for i, row in metadata_df.iterrows():

        if int(row["SAMPLEID"]) == int(sampleID):
            item = {"AGE":row["AGE"], "BBTYPE": row["BBTYPE"], "ETHNICITY": row["ETHNICITY"], "GENDER": row["GENDER"], "LOCATION": row["LOCATION"], "SAMPLEID": row["SAMPLEID"]}
            metadata_list.append(item)

    def saveOutput(data):
            with open('bellybutton_metadata.txt', 'w') as outfile:
                json.dump(data, outfile, sort_keys = True, indent = 2)

    saveOutput(metadata_list)
    return (metadata_list)

def wfreq(sampleName):
    metadata = os.path.join('data', 'Belly_Button_Biodiversity_Metadata.csv')
    metadata_df = pd.read_csv(metadata)
    sample_list = sampleName.split('_')
    sampleID = int(sample_list[1])
    wfreq_list = []
    for i, row in metadata_df.iterrows():

        if int(row["SAMPLEID"]) == int(sampleID):
            item = row["WFREQ"]
            wfreq_list.append(item)

    def saveOutput(data):
            with open('bellybutton_wfreq.txt', 'w') as outfile:
                json.dump(data, outfile, sort_keys = True, indent = 2)

    saveOutput(wfreq_list)
    return (wfreq_list)

#testing in ipynb and just need to sort on sample column

def otuValues(sampleName):
    samples = os.path.join('data', 'samples_data.csv')
    samples_df = pd.read_csv(samples)
    samples_input_df = pd.DataFrame(samples_df[sampleName],samples_df["otu_id"])
    samples_input_df.sort_values(sampleName, inplace=True, ascending=False)
    samples_input_df.fillna(0, inplace=True)
    otu_id_list = samples_input_df.index.tolist()
    sorted_samples = samples_input_df[sampleName].tolist()

    sorted_samples_dict = {"otu_id": otu_id_list, "sample_values": sorted_samples}
    sorted_samples_list = []
    sorted_samples_list.append(sorted_samples_dict)

    def saveOutput(data):
            with open('bellybutton_otu_samples.txt', 'w') as outfile:
                json.dump(data, outfile, sort_keys = True, indent = 2)

    saveOutput(sorted_samples_list)
    return sorted_samples_dict    