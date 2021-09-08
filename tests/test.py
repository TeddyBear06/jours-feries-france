# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from datetime import date

from jours_feries_france import JoursFeries


class TestDatasetParser(unittest.TestCase):
    def test_validates_region(self):
        with self.assertRaises(ValueError):
            JoursFeries.for_year(2018, zone="foo")

    def test_is_bank_holiday(self):
        self.assertTrue(JoursFeries.is_bank_holiday(date(2019, 12, 25)))
        self.assertTrue(
            JoursFeries.is_bank_holiday(date(2019, 12, 25), zone="Métropole")
        )
        self.assertTrue(
            JoursFeries.is_bank_holiday(date(2019, 12, 26), zone="Alsace-Moselle")
        )

        self.assertFalse(JoursFeries.is_bank_holiday(date(2019, 12, 26)))
        self.assertFalse(
            JoursFeries.is_bank_holiday(date(2019, 12, 26), zone="Métropole")
        )

    def test_next_bank_holiday(self):
        self.assertEquals(
            ("11 novembre", date(2018, 11, 11)),
            JoursFeries.next_bank_holiday(date(2018, 11, 10)),
        )

        self.assertEquals(
            ("11 novembre", date(2018, 11, 11)),
            JoursFeries.next_bank_holiday(date(2018, 11, 11), zone="Métropole"),
        )

        self.assertEquals(
            ("Jour de Noël", date(2018, 12, 25)),
            JoursFeries.next_bank_holiday(date(2018, 12, 11), zone="Métropole"),
        )

    def test_for_year(self):
        self.assertDictEqual(
            JoursFeries.for_year(2018),
            {
                "1er janvier": date(2018, 1, 1),
                "Lundi de Pâques": date(2018, 4, 2),
                "1er mai": date(2018, 5, 1),
                "8 mai": date(2018, 5, 8),
                "Ascension": date(2018, 5, 10),
                "Lundi de Pentecôte": date(2018, 5, 21),
                "14 juillet": date(2018, 7, 14),
                "Assomption": date(2018, 8, 15),
                "Toussaint": date(2018, 11, 1),
                "11 novembre": date(2018, 11, 11),
                "Jour de Noël": date(2018, 12, 25),
            },
        )

        self.assertDictEqual(
            JoursFeries.for_year(2020),
            {
                "11 novembre": date(2020, 11, 11),
                "Ascension": date(2020, 5, 21),
                "Assomption": date(2020, 8, 15),
                "14 juillet": date(2020, 7, 14),
                "1er mai": date(2020, 5, 1),
                "1er janvier": date(2020, 1, 1),
                "Lundi de Pâques": date(2020, 4, 13),
                "Jour de Noël": date(2020, 12, 25),
                "Lundi de Pentecôte": date(2020, 6, 1),
                "Toussaint": date(2020, 11, 1),
                "8 mai": date(2020, 5, 8),
            },
        )

    def test_for_year_in_alsace(self):
        self.assertDictEqual(
            JoursFeries.for_year(2018, zone="Alsace-Moselle"),
            {
                "11 novembre": date(2018, 11, 11),
                "Ascension": date(2018, 5, 10),
                "Assomption": date(2018, 8, 15),
                "14 juillet": date(2018, 7, 14),
                "1er mai": date(2018, 5, 1),
                "1er janvier": date(2018, 1, 1),
                "Lundi de Pâques": date(2018, 4, 2),
                "Jour de Noël": date(2018, 12, 25),
                "Lundi de Pentecôte": date(2018, 5, 21),
                "Toussaint": date(2018, 11, 1),
                "8 mai": date(2018, 5, 8),
                "Vendredi saint": date(2018, 3, 30),
                "2ème jour de Noël": date(2018, 12, 26),
            },
        )

        self.assertDictEqual(
            JoursFeries.for_year(2020, zone="Alsace-Moselle"),
            {
                "11 novembre": date(2020, 11, 11),
                "Ascension": date(2020, 5, 21),
                "Assomption": date(2020, 8, 15),
                "14 juillet": date(2020, 7, 14),
                "1er mai": date(2020, 5, 1),
                "1er janvier": date(2020, 1, 1),
                "Lundi de Pâques": date(2020, 4, 13),
                "Jour de Noël": date(2020, 12, 25),
                "Lundi de Pentecôte": date(2020, 6, 1),
                "Toussaint": date(2020, 11, 1),
                "8 mai": date(2020, 5, 8),
                "Vendredi saint": date(2020, 4, 10),
                "2ème jour de Noël": date(2020, 12, 26),
            },
        )

    def testPaques(self):
        self.assertEquals(JoursFeries.paques(1954), date(1954, 4, 18))
        self.assertEquals(JoursFeries.paques(1981), date(1981, 4, 19))
        self.assertEquals(JoursFeries.paques(2049), date(2049, 4, 18))

    def testNamesAllZones(self):
        def names(holidays):
            return set(holidays.keys())

        base = set(
            [
                "1er janvier",
                "1er mai",
                "8 mai",
                "14 juillet",
                "Assomption",
                "Toussaint",
                "11 novembre",
                "Jour de Noël",
                "Lundi de Pâques",
                "Ascension",
                "Lundi de Pentecôte",
            ]
        )

        extra_holidays = [
            ["Alsace-Moselle", set(["Vendredi saint", "2ème jour de Noël"])],
            ["Guadeloupe", set(["Abolition de l'esclavage"])],
            ["Guyane", set(["Abolition de l'esclavage"])],
            ["Martinique", set(["Abolition de l'esclavage"])],
            ["Mayotte", set(["Abolition de l'esclavage"])],
            ["Nouvelle-Calédonie", set()],
            ["La Réunion", set(["Abolition de l'esclavage"])],
            ["Polynésie Française", set()],
            ["Saint-Barthélémy", set(["Abolition de l'esclavage"])],
            ["Saint-Martin", set(["Abolition de l'esclavage"])],
            ["Wallis-et-Futuna", set()],
            ["Saint-Pierre-et-Miquelon", set()],
        ]

        self.assertSetEqual(names(JoursFeries.for_year(2020, "Métropole")), base)

        for test in extra_holidays:
            zone, holidays = test
            self.assertEquals(
                names(JoursFeries.for_year(2020, zone)), base.union(holidays)
            )

        self.assertEquals(
            JoursFeries.ZONES, ["Métropole"] + [e[0] for e in extra_holidays]
        )

    def testAbolition_esclavage(self):
        tests = [
            ("Mayotte", date(2020, 4, 27)),
            ("Martinique", date(2020, 5, 22)),
            ("Guadeloupe", date(2020, 5, 27)),
            ("Saint-Martin", date(2020, 5, 28)),
            ("Guyane", date(2020, 6, 10)),
            ("Saint-Barthélémy", date(2020, 10, 9)),
            ("La Réunion", date(2020, 12, 20)),
        ]

        zones = set()
        for test in tests:
            zone, expected_date = test
            zones.add(zone)
            self.assertEquals(
                JoursFeries.abolition_esclavage(2020, zone), expected_date
            )

        for zone in [z for z in JoursFeries.ZONES if z not in zones]:
            self.assertEquals(JoursFeries.abolition_esclavage(2020, zone), None)

        # Saint-Martin
        self.assertEquals(
            JoursFeries.abolition_esclavage(2017, "Saint-Martin"), date(2017, 5, 27)
        )
        self.assertEquals(
            JoursFeries.abolition_esclavage(2018, "Saint-Martin"), date(2018, 5, 28)
        )

        # Gestion des dates antérieures au décret officiel relatif à la commémoration de l'abolition de l'esclavage
        # https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000336997/

        # Mayotte
        self.assertEquals(
            JoursFeries.abolition_esclavage(1982, "Mayotte"), None
        )
        self.assertEquals(
            JoursFeries.abolition_esclavage(1983, "Mayotte"), date(1983, 4, 27)
        )

        # Martinique
        self.assertEquals(
            JoursFeries.abolition_esclavage(1982, "Martinique"), None
        )
        self.assertEquals(
            JoursFeries.abolition_esclavage(1983, "Martinique"), date(1983, 5, 22)
        )

        # Guadeloupe
        self.assertEquals(
            JoursFeries.abolition_esclavage(1982, "Guadeloupe"), None
        )
        self.assertEquals(
            JoursFeries.abolition_esclavage(1983, "Guadeloupe"), date(1983, 5, 27)
        )

        # Saint-Martin
        self.assertEquals(
            JoursFeries.abolition_esclavage(1982, "Saint-Martin"), None
        )
        self.assertEquals(
            JoursFeries.abolition_esclavage(1983, "Saint-Martin"), date(1983, 5, 27)
        )

        # Guyane
        self.assertEquals(
            JoursFeries.abolition_esclavage(1982, "Guyane"), None
        )
        self.assertEquals(
            JoursFeries.abolition_esclavage(1983, "Guyane"), date(1983, 6, 10)
        )

        # Saint-Barthélémy
        self.assertEquals(
            JoursFeries.abolition_esclavage(1982, "Saint-Barthélémy"), None
        )
        self.assertEquals(
            JoursFeries.abolition_esclavage(1983, "Saint-Barthélémy"), date(1983, 10, 9)
        )

        # La Réunion
        self.assertEquals(
            JoursFeries.abolition_esclavage(1980, "La Réunion"), None
        )
        self.assertEquals(
            JoursFeries.abolition_esclavage(1981, "La Réunion"), date(1981, 12, 20)
        )
