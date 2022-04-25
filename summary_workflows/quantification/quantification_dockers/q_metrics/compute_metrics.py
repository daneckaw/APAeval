#!/usr/bin/env python3

from __future__ import division
import io
import os
import json
from argparse import ArgumentParser
from JSON_templates import JSON_templates
from matchPAS import matchPAS

def main(args):

    # input parameters
    participant_input = args.participant_data
    gold_standards_dir = args.gold_standards_dir
    challenge_ids = args.challenge_ids
    participant = args.participant_name
    community = args.community_name
    out_path = args.output
    window = args.window

    # Assuring the output path does exist
    if not os.path.exists(os.path.dirname(out_path)):
        try:
            os.makedirs(os.path.dirname(out_path))
            with open(out_path, mode="a"):
                pass
        except OSError as exc:
            print("OS error: {0}".format(exc) + "\nCould not create output path: " + out_path)

    compute_metrics(participant_input, gold_standards_dir, challenge_ids, participant, community, out_path, window)


def compute_metrics(participant_input, gold_standards_dir, challenge_ids, participant, community, out_path, window):

    # define array that will hold the full set of assessment datasets
    ALL_ASSESSMENTS = []

    for challenge in challenge_ids:
        
        gold_standard = os.path.join(gold_standards_dir, challenge + ".bed")

        # metric on the number of matched sites
        match_with_gt_run = matchPAS.match_with_gt(participant_input,gold_standard,window)
        merged_bed_df, expression_unmatched = match_with_gt_run[0], match_with_gt_run[1]

        # metric on correlation coffecient
        correlation= matchPAS.corr_with_gt(merged_bed_df)

        # get json assessment file for both metrics
        data_id_1 = community + ":" + challenge + "_expression_unmatched_" + participant
        std_error= 0
        assessment_matched_sites = JSON_templates.write_assessment_dataset(data_id_1, community, challenge, participant, "expression_unmatched", expression_unmatched, std_error)

        data_id_2 = community + ":" + challenge + "_correlation_" + participant
        std_error= 0
        assessment_correlation = JSON_templates.write_assessment_dataset(data_id_2, community, challenge, participant, "correlation", correlation, std_error)

        # push the two assessment datasets to the main dataset array
        ALL_ASSESSMENTS.extend([assessment_matched_sites, assessment_correlation])

    # once all assessments have been added, print to json file
    with io.open(out_path,
                 mode='w', encoding="utf-8") as f:
        jdata = json.dumps(ALL_ASSESSMENTS, sort_keys=True, indent=4, separators=(',', ': '))
        f.write(jdata)


if __name__ == '__main__':
    
    parser = ArgumentParser()
    parser.add_argument("-i", "--participant_data", help="execution workflow prediction outputs", required=True)
    parser.add_argument("-c", "---challenge_ids", nargs='+', help="List of challenge ids selected by the user, separated by spaces", required=True)
    parser.add_argument("-g", "--gold_standards_dir", help="dir that contains gold standard datasets for current challenge", required=True)
    parser.add_argument("-p", "--participant_name", help="name of the tool used for prediction", required=True)
    parser.add_argument("-com", "--community_name", help="name/id of benchmarking community", required=True)
    parser.add_argument("-o", "--output", help="output path where assessment JSON files will be written", required=True)
    parser.add_argument("-w", "--window", help="window (nt) for scanning for poly(A) sites", required=True, type=int)
    
    args = parser.parse_args()

    
    main(args)




