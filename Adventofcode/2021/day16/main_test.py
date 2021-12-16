import unittest
from main import PacketFactory, LiteralPacket, OperatorPacket, hex_to_bin_stream, parse_packet

class MainTest(unittest.TestCase):
    def test_hex_to_bin_stream(self):
        bits = ''.join(hex_to_bin_stream('D2FE28'))
        self.assertEqual(bits, '110100101111111000101000')

    def test_packet_factor_literal(self):
        packet = PacketFactory(iter('110100101111111000101000'))
        self.assertIsInstance(packet, LiteralPacket)
        self.assertEqual(packet.version, 6) 
        self.assertEqual(packet.type_id, 4) 
        if isinstance(packet, LiteralPacket):
            # we know it is, otherwise test would fail earlier
            # just to remove the annoying lsp warnings
            self.assertEqual(packet.value, 2021) 

    def test_packet_factor_operator_mode_0(self):
        packet = PacketFactory(iter('00111000000000000110111101000101001010010001001000000000'))
        self.assertIsInstance(packet, OperatorPacket)
        self.assertEqual(packet.version, 1) 
        self.assertEqual(packet.type_id, 6) 
        if isinstance(packet, OperatorPacket):
            # we know it is, otherwise test would fail earlier
            # just to remove the annoying lsp warnings
            self.assertEqual(len(packet.subpackets), 2)
            self.assertEqual(packet.subpackets[0].value, 10) 
            self.assertEqual(packet.subpackets[1].value, 20) 

    def test_packet_factor_operator_mode_1(self):
        packet = PacketFactory(hex_to_bin_stream('EE00D40C823060'))
        self.assertIsInstance(packet, OperatorPacket)
        self.assertEqual(packet.version, 7) 
        self.assertEqual(packet.type_id, 3) 
        if isinstance(packet, OperatorPacket):
            # we know it is, otherwise test would fail earlier
            # just to remove the annoying lsp warnings
            self.assertEqual(len(packet.subpackets), 3)
            self.assertEqual(packet.subpackets[0].value, 1) 
            self.assertEqual(packet.subpackets[1].value, 2) 
            self.assertEqual(packet.subpackets[2].value, 3) 

    def test_example_1_solution_part_1(self):
        packet = parse_packet(iter(['8A004A801A8002F478']))
        r = packet.version_sum()
        self.assertEqual(r, 16)

    def test_example_2_solution_part_1(self):
        packet = parse_packet(iter(['620080001611562C8802118E34']))
        r = packet.version_sum()
        self.assertEqual(r, 12)

    def test_example_3_solution_part_1(self):
        packet = parse_packet(iter(['C0015000016115A2E0802F182340']))
        r = packet.version_sum()
        self.assertEqual(r, 23)

    def test_example_4_solution_part_1(self):
        packet = parse_packet(iter(['A0016C880162017C3686B18A3D4780']))
        r = packet.version_sum()
        self.assertEqual(r, 31)

    def test_example_1_solution_part_2(self):
        packet = parse_packet(iter(['C200B40A82']))
        self.assertEqual(packet.value, 3)

    def test_example_2_solution_part_2(self):
        packet = parse_packet(iter(['04005AC33890']))
        self.assertEqual(packet.value, 54)

    def test_example_3_solution_part_2(self):
        packet = parse_packet(iter(['880086C3E88112']))
        self.assertEqual(packet.value, 7)

    def test_example_4_solution_part_2(self):
        packet = parse_packet(iter(['CE00C43D881120']))
        self.assertEqual(packet.value, 9)

    def test_example_5_solution_part_2(self):
        packet = parse_packet(iter(['D8005AC2A8F0']))
        self.assertEqual(packet.value, 1)

    def test_example_6_solution_part_2(self):
        packet = parse_packet(iter(['F600BC2D8F']))
        self.assertEqual(packet.value, 0)

    def test_example_7_solution_part_2(self):
        packet = parse_packet(iter(['9C005AC2F8F0']))
        self.assertEqual(packet.value, 0)

    def test_example_8_solution_part_2(self):
        packet = parse_packet(iter(['9C0141080250320F1802104A08']))
        self.assertEqual(packet.value, 1)


if __name__ == '__main__':
    unittest.main()
