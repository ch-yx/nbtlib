
from nbtlib.nbt import File
from nbtlib.tag import *


__all__ = ['bytes_for_valid_tags', 'nbt_files']


bytes_for_valid_tags = [

    # Byte tag
    (b'\x00', Byte(0)),
    (b'\xFF', Byte(-1)),
    (b'\x7F', Byte(127)),
    (b'\x80', Byte(-128)),

    # Short tag
    (b'\x00\x00', Short(0)),
    (b'\xFF\xFF', Short(-1)),
    (b'\x7F\xFF', Short(32767)),
    (b'\x80\x00', Short(-32768)),

    # Int tag
    (b'\x00\x00\x00\x00', Int(0)),
    (b'\xFF\xFF\xFF\xFF', Int(-1)),
    (b'\x7F\xFF\xFF\xFF', Int(2147483647)),
    (b'\x80\x00\x00\x00', Int(-2147483648)),

    # Long tag
    (b'\x00\x00\x00\x00\x00\x00\x00\x00', Long(0)),
    (b'\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF', Long(-1)),
    (b'\x7F\xFF\xFF\xFF\xFF\xFF\xFF\xFF', Long(9223372036854775807)),
    (b'\x80\x00\x00\x00\x00\x00\x00\x00', Long(-9223372036854775808)),

    # Float tag
    (b'\x00\x00\x00\x00', Float(0)),
    (b'\xbf\x80\x00\x00', Float(-1)),
    (b'>\xff\x182',       Float(0.49823147058486938)),

    # Double tag
    (b'\x00\x00\x00\x00\x00\x00\x00\x00', Double(0)),
    (b'\xbf\xf0\x00\x00\x00\x00\x00\x00', Double(-1)),
    (b'?\xdf\x8fk\xbb\xffj^',             Double(0.49312871321823148)),

    # ByteArray tag
    (b'\x00\x00\x00\x00',             ByteArray([])),
    (b'\x00\x00\x00\x01\xff',         ByteArray([-1])),
    (b'\x00\x00\x00\x03\x01\x02\x03', ByteArray([1, 2, 3])),

    # String tag
    (b'\x00\x00',                         String('')),
    (b'\x00\x0bhello world',              String('hello world')),
    (b'\x00\x06\xc3\x85\xc3\x84\xc3\x96', String('ÅÄÖ')),

    # List tag
    (b'\x02\x00\x00\x00\x00',                           List[Short]([])),
    (b'\x01\x00\x00\x00\x04\x05\xf7\x12\x40',           List[Byte]([Byte(5), Byte(-9), Byte(18), Byte(64)])),
    (b'\x08\x00\x00\x00\x02\x00\x05hello\x00\x05world', List[String]([String('hello'), String('world')])),

    # Compound tag
    (b'\x00',                                   Compound({})),
    (b'\x03\x00\x03foo\x00\x00\x00*\x00',       Compound({'foo': Int(42)})),
    (b'\x01\x00\x01a\x00\x01\x00\x01b\x01\x00', Compound({'a': Byte(0), 'b': Byte(1)})),

    # IntArray tag
    (b'\x00\x00\x00\x00',                                 IntArray([])),
    (b'\x00\x00\x00\x01\xff\xff\xff\xff',                 IntArray([-1])),
    (b'\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02', IntArray([1, 2])),

]


nbt_files = [

    (
        'tests/nbt_files/hello_world.nbt', File({'hello world': Compound({
            'name': String('Bananrama')
        })})
    ),

    (
        'tests/nbt_files/bigtest.nbt', File({'Level': Compound({
            'nested compound test': Compound({
                'egg': Compound({
                    'name': String('Eggbert'), 'value': Float(0.5)
                }),
                'ham': Compound({
                    'name': String('Hampus'), 'value': Float(0.75)
                })
            }),
            'intTest': Int(2147483647),
            'byteTest': Byte(127),
            'stringTest': String('HELLO WORLD THIS IS A TEST STRING ÅÄÖ!'),
            'listTest (long)': List[Long]([11, 12, 13, 14, 15]),
            'doubleTest': Double(0.49312871321823148),
            'floatTest': Float(0.49823147058486938),
            'longTest': Long(9223372036854775807),
            'listTest (compound)': List[Compound]([
                Compound({
                    'created-on': Long(1264099775885),
                    'name': String('Compound tag #0')
                }),
                Compound({
                    'created-on': Long(1264099775885),
                    'name': String('Compound tag #1')
                })
            ]),
            'byteArrayTest (the first 1000 values of (n*n*255+n*7)%100, starting with n=0 (0, 62, 34, 16, 8, ...))': ByteArray(
                (n**2 * 255 + n*7) % 100 for n in range(1000)
            ),
            'shortTest': Short(32767)
        })}, gzipped=True)
    ),

]