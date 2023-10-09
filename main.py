"""
Gale Shapley Algorithm with Polygamy
Assignent 2: Stable Matching
CSE 551
Author: Rohan Rele
"""


def gale_shapley_polygamous(hospital_table, resident_table):
    hospitals_with_open_positions = [key for key in
                                     hospital_table.keys()]  # create a queue from the keys of the hospitals' preference dictionary
    hospital_counts = {key: val[1] for key, val in hospital_table.items()}  # create array of counts for each hospital
    resident_matched = {key: -1 for key in resident_table}  # create matching S keyed by residents
    # we could also potentially do: [(key,val[1]) for key, val in hospital_table.items()]

    while hospitals_with_open_positions:
        hi = hospitals_with_open_positions.pop(0)  # set current hospital
        curr_hospital_pref_list = hospital_table[hi][0]  # obtain current hospitals applicant ranking
        rj = curr_hospital_pref_list.pop(0)  # find most 'attractive' resident to hospital i

        if resident_matched[rj] == -1:  # if resident j is free
            resident_matched[rj] = hi  # match hospital i to resident j
            hospital_counts[hi] = hospital_counts[hi] - 1
        else:
            rj_pref_list = resident_table[rj]  # get resident j's preference list
            hk = resident_matched[rj]  # get the hospital k that resident j is current matched to
            if rj_pref_list[hk - 1] < rj_pref_list[
                hi - 1]:  # if resident j prefers hospital k, who he/she is current matched to, to hospital i,
                pass  # do nothing i.e., leave matching as is
            else:  # if resident j prefers hospital i to its current matching, hospital j,
                resident_matched[rj] = hi  # re-match resident j to hospital i
                hospital_counts[hk] = hospital_counts[hk] + 1  # make one new position available at hospital k
                hospital_counts[hi] = hospital_counts[
                                          hi] - 1  # decrease the number of open positions at hospital i by 1

        hospitals_with_open_positions = [key for key, val in hospital_counts.items() if val > 0]

    return resident_matched


hospital_table_example = {1: [[3, 2, 1, 6, 7, 4, 5], 3],
                          2: [[1, 3, 7, 6, 5, 4, 2], 2],
                          3: [[1, 6, 4, 2, 3, 7, 5], 2]
                          }

resident_table_example = {1: [1, 3, 2],
                          # for r1: 1st hospital is their 1st choice, 2nd hospital is their 3rd choice, 3rd hospital is their 2nd choice
                          2: [3, 2, 1],
                          # for r2: 1st hospital is their 3rd choice, 2nd hospital is their 2nd choice, 3rd hospital is their 1st choice
                          3: [1, 2, 3],
                          # ... keeps going like that since the RESIDENTS are the ones being PROPOSED to ...
                          4: [2, 3, 1],
                          5: [3, 2, 1],
                          6: [2, 1, 3],
                          7: [2, 1, 3]
                          }

result = gale_shapley_polygamous(hospital_table_example, resident_table_example)
for r, h in result.items():
    print("(", r, ",", h, ")")
