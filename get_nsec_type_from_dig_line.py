#!/usr/bin/env python3
import fileinput
import sys

total_count = 0
nsec3_count = 0
nsec_dict = {}

for line in fileinput.input():
    #print(line)
    sline = line.strip()
    if sline == "":
        continue
    split_line = sline.split()
    #print(split_line)
    if len(split_line) < 4:
        continue
    total_count += 1
    domain = split_line[0]
    nsec_type = split_line[3]
    if domain.startswith("a."):
        true_domain = domain[2:]
    elif nsec_type == "NSEC3":
        true_domain = ".".join(domain.split(".")[1:])
    else:
        # The domain was not the a. subdomain we asked for or an NSEC3 hashed domain.
        # Some servers can return extra stuff. To avoid double counting we ignore.
        #print(line, end='')
        continue
    if true_domain not in nsec_dict:
        nsec_dict[true_domain] = set()
    nsec_dict[true_domain].add(nsec_type)

domains_with_only_nsec3 = 0
domains_with_only_nsec = 0
domains_with_both = 0
total_distinct_domains = 0
for domain in nsec_dict:
    domain_set = nsec_dict[domain]
    if "NSEC" in domain_set and "NSEC3" not in domain_set:
        domains_with_only_nsec += 1
    if "NSEC3" in domain_set and "NSEC" not in domain_set:
        domains_with_only_nsec3 += 1
    if "NSEC3" in domain_set and "NSEC" in domain_set:
        domains_with_both += 1
    total_distinct_domains += 1
    print(f"{domain},{'NSEC' if 'NSEC' in nsec_dict[domain] else ''},{'NSEC3' if 'NSEC3' in nsec_dict[domain] else ''}")
print(f"Of the {total_distinct_domains} distinct domains measured: {domains_with_only_nsec3}/{total_distinct_domains} only used NSEC3, {domains_with_only_nsec}/{total_distinct_domains} only used NSEC, {domains_with_both}/{total_distinct_domains} used both.", file=sys.stderr)