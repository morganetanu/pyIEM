"""Tests for the DS3505 format"""
import unittest
import os

from pyiem.ncei.ds3505 import parser


def get_file(name):
    ''' Helper function to get the text file contents '''
    basedir = os.path.dirname(__file__)
    fn = "%s/../../../data/product_examples/NCEI/%s" % (basedir, name)
    return open(fn)


class DS3505(unittest.TestCase):
    """Go for it"""

    def test_171024(self):
        """Bad parse for ALO"""
        msg = ("0088999999949101950010113005+42550-092400SAO  +026599999V02"
               "099999000050000049N000000599+00224+00175999999EQDN01 00000"
               "JPWTH 1QNNG11 1 00000K11 1 00035L11 1 00000N11 1 00000S11 "
               "1 00036W11 1 00000")
        data = parser(msg, 'ALO', add_metar=True)
        self.assertEqual(data['metar'],
                         ("ALO 011300Z AUTO 0SM 02/02 RMK T00220017 IEM_DS3505"
                          ))

    def test_badtemp(self):
        """Station had obviously bad temperature, see what QC said"""
        msg = ("0171030750999992005041908204+58450-003083FM-15+0036EGPC "
               "V0201401N004612200019N0112651N1+99999+99999999999ADDGA1021"
               "+009609999GF102991999999999999999999MA1100911999999MW1001"
               "REMMET045EGPC 190820Z 14009KT 9999 FEW032 35/33 Q1009;"
               "EQDQ01+003503ATOT  Q02+003303ATOD  Q03+000000PRSWM2")
        data = parser(msg, 'EGPC', add_metar=True)
        self.assertEqual(data['metar'],
                         ("EGPC 190820Z AUTO 14009KT 7SM A2980 RMK IEM_DS3505"
                          ))

    def test_altimeter(self):
        """See what we are doing with altimeter and SLP"""
        msg = ("0125030750999992013102322004+58450-003083FM-12+003699999"
               "V0202501N009819999999N030000199+00671+00351099051ADDMA"
               "1999990098611MD1110201+9990OD139901441999REMSYN07003075 "
               "45980 /2519 10067 20035 39861 49905 51020 333 8//99 90710 "
               "91128=")
        data = parser(msg, 'EGPC', add_metar=True)
        self.assertEqual(data['metar'],
                         ("EGPC 232200Z AUTO 25019KT 19SM 07/04 RMK SLP905 "
                          "T00670035 51020 IEM_DS3505"
                          ))

    def test_6hour_temp(self):
        """6 hour high/low"""
        # 2016-08-12 23:53:00
        # KAMW 122353Z AUTO 35014G23KT 10SM CLR 25/21 A2983 RMK AO2 SLP092
        # 60000 T02500211 10272 20250 55001
        msg = ("0271725472949892016081223537+41991-093619FM-15+0291KAMW V03035"
               "05N007252200059N0160935N5+02505+02115100925ADDAA101000095AA206"
               "000021GA1005+999999999GD10991+9999999GF1009919999999999999999"
               "99KA1060M+02721KA2060N+02501MA1101025097575MD1590019+9999"
               "OC101185REMMET11708/12/16 17:53:02 METAR KAMW 122353Z "
               "35014G23KT 10SM CLR 25/21 A2983 RMK AO2 SLP092 60000 "
               "T02500211 10272 20250 55001")
        data = parser(msg, 'KAMW', add_metar=True)
        self.assertEqual(data['metar'],
                         ("KAMW 122353Z AUTO 35014G23KT 10SM CLR 25/21 A2983 "
                          "RMK 60000 SLP092 T02500211 10272 20250 55001 "
                          "IEM_DS3505"))

    def test_precip_6group(self):
        """3 hour precip"""
        # 2016-08-12 02:53:00
        # KAMW 120253Z AUTO 36012KT 1 1/4SM +TSRA BR SCT005
        # SCT009 OVC014 21/21 A2991 RMK AO2 WSHFT 0219 LTG DSNT ALQDS
        # RAE00B24 TSE0155B27 SLP119 P0080 60232 T02110211 53037
        msg = ("0463725472949892016081202537+41991-093619FM-15+0291KAMW V03"
               "03605N00625004275MN0020125N5+02115+02115101195ADDAA10102069"
               "5AA203058991AU107000025AU230020035AU300001015AW1105AW2635AW"
               "3905AW4951GA1045+001525999GA2045+002745999GA3085+004275999"
               "GD12991+0015259GD22991+0027459GD34991+0042759GE19MSL   "
               "+99999+99999GF199999999999001521999999MA1101295097845"
               "MD1390379+9999REMMET18308/11/16 20:53:02 METAR KAMW "
               "120253Z 36012KT 1 1/4SM +TSRA BR SCT005 SCT009 "
               "OVC014 21/21 A2991 RMK AO2 WSHFT 0219 LTG DSNT "
               "ALQDS RAE00B24 TSE0155B27 SLP119 P0080 60232 "
               "T02110211 53037EQDQ01  05898PRCP03")
        data = parser(msg, 'KAMW', add_metar=True)
        # NOTE, this should be 0.80 instead of 0.81 !?!?!, NCDC wrong?
        self.assertEqual(data['metar'],
                         ("KAMW 120253Z AUTO 36012KT 1 1/4SM +TSRA BR "
                          "SCT005 SCT009 OVC014 21/21 A2991 RMK P0081 60232 "
                          "SLP119 T02110211 53037 IEM_DS3505"))

    def test_metar(self):
        """Can we replicate an actual METAR"""
        # IEM METAR database has this for 1 Jan 2016
        # KAMW 010713Z AUTO 29013KT 10SM BKN017 OVC033 M05/M08 A3028 RMK
        #    AO2 T10501083
        msg = ("0232725472949892016010107137+41991-093619FM-16+0291KAMW "
               "V0302905N00675005185MN0160935N5-00505-00835999999ADDGA1075+"
               "005185999GA2085+010065999GD13991+0051859GD24991+0100659"
               "GE19MSL   +99999+99999GF199999999999005181999999MA1102545"
               "099065REMMET09501/01/16 01:13:02 SPECI KAMW 010713Z "
               "29013KT 10SM BKN017 OVC033 M05/M08 A3028 RMK AO2 T10501083")
        data = parser(msg, 'KAMW', add_metar=True)
        self.assertEqual(data['metar'],
                         ("KAMW 010713Z AUTO 29013KT 10SM BKN017 OVC033 "
                          "M05/M08 A3028 RMK T10501083 IEM_DS3505"))

    def test_metar2(self):
        """Can we do more"""
        # KAMW 010853Z AUTO 30013KT 10SM OVC017 M05/M08 A3028 RMK
        #    AO2 SLP266 T10501083 55004
        msg = ("0232725472949892016010108537+41991-093619FM-15+0291KAMW "
               "V0303005N00675005185MN0160935N5-00505-00835102665ADDAA1"
               "01000095GA1085+005185999GD14991+0051859GE19MSL   +99999+"
               "99999GF199999999999005181999999MA1102545099065MD1590049+"
               "9999REMMET10101/01/16 02:53:02 METAR KAMW 010853Z 30013KT "
               "10SM OVC017 M05/M08 A3028 RMK AO2 SLP266 T10501083 55004")
        data = parser(msg, 'KAMW', add_metar=True)
        self.assertEqual(data['metar'],
                         ("KAMW 010853Z AUTO 30013KT 10SM OVC017 M05/M08 "
                          "A3028 RMK SLP266 T10501083 55004 IEM_DS3505"))

    def test_171023(self):
        """This failed"""
        msg = ("0174030750999991977080406004+58450-003083FM-12+0039EGPC "
               "V0209991C00001066001CN0750001N9+00901+00801101131ADDAJ10000"
               "9199999999AY111999GA1011+006009089GA2031+036009039GA3061+"
               "066009029GF107991021081008001031061MD1710131+9999MW1021WG"
               "199999999999REMSYN02920310 70307 81820 83362 86272")
        data = parser(msg, 'KAMW', add_metar=True)
        self.assertTrue(data is not None)

        msg = ("0067030750999991999102018004+58450-003080FM-12+0039EGPC "
               "V02099999999999999999N9999999N1+99999+99999999999REMSYN058"
               "AAXX  20184 03075 46/// ///// 1//// 2//// 4//// 5//// 333;")
        data = parser(msg, 'EGPC', add_metar=True)
        self.assertTrue(data is not None)

    def test_basic(self):
        """Can we parse it, yes we can"""
        msg = ("0114010010999991988010100004+70933-008667FM-12+0009ENJA "
               "V0203301N01851220001CN0030001N9-02011-02211100211ADDAA10"
               "6000091AG14000AY131061AY221061GF102991021051008001001001"
               "MD1710141+9999MW1381OA149902631REMSYN011333   91151")
        data = parser(msg, 'ENJA', add_metar=True)
        self.assertTrue(data is not None)
        self.assertEqual(data['metar'],
                         ('ENJA 010000Z AUTO 33036KT 2SM '
                          'M20/M22 RMK SLP021 T12011221 57014 IEM_DS3505'))

    def test_read(self):
        """Can we process an entire file?"""
        for line in get_file("DS3505.txt"):
            data = parser(line.strip(), 'ENJA')
            self.assertTrue(data is not None)

        for line in get_file("DS3505_KAMW_2016.txt"):
            data = parser(line.strip(), 'KAMW')
            self.assertTrue(data is not None)