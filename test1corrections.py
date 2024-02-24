#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 00:21:54 2024

@author: anniereynolds
"""


def unique_families(protein_names):
    return len({protein[:-2] for protein in protein_names})


def family_counts(protein_names):
    counts = {}
    for protein in protein_names:
        family, _revision = protein.split(".")
        counts[family] = counts.get(family, 0) + 1
    return counts


def join_dictionaries(counts, more_counts):
    for family, count in more_counts.items():
        counts[family] = counts.get(family, 0) + count
    return counts


MONTHS = {"January": "01", "February": "02", "March": "03", "April": "04",
          "May": "05", "June": "06", "July": "07", "August": "08", "September":
              "09", "October": "10", "November": "11", "December": "12"}


def dates_to_iso(dates):
    iso_dates = []
    for date in dates:
        print(date)
        month, day, year = date.split()
        day = day[:-1]
        if len(day) < 2:
            day = "0" + day
        month = MONTHS[month]
        iso_dates.append("-".join((year, month, day)))
    return iso_dates


def chronological(dates):
    iso_dates = dates_to_iso(dates)
    iso_to_written = {}
    for i, date in enumerate(dates):
        iso_to_written[iso_dates[i]] = date
    iso_dates.sort()
    return [iso_to_written[iso] for iso in iso_dates]
