from collections import defaultdict
from itertools import islice


def rail_sequence(n):
    rail = 1
    rail_inc = 1

    yield rail

    while True:
        if not 1 <= (rail + rail_inc) <= n:
            rail_inc *= -1

        rail += rail_inc

        yield rail


def next_chars(n, iterable):
    return ''.join(islice(iterable, n))


def split_rails(encoded, n):
    # Cycle length is 2(n-1)
    # If there are remainders, they are added to the rail in rail sequence
    # order, making each section of the string longer by 1 or 2
    print(f"splitting {encoded} into {n} rails")
    cycle_length = 2 * (n - 1)
    encoded_len = len(encoded)
    num_cycles, remainder = divmod(encoded_len, cycle_length)
    print(f"l {encoded_len} cycle {cycle_length} "
          f"num {num_cycles} + {remainder}")

    # Start out with a complete cycle
    rail_lengths = {x: num_cycles * 2 for x in range(2, n)}
    rail_lengths[1] = num_cycles
    rail_lengths[n] = num_cycles

    # Now add to each rail's length if there are remainders
    rail_seq = rail_sequence(n)
    for i in range(remainder):
        rail_lengths[next(rail_seq)] += 1
    """ if remainder:
        raise NotImplementedError
    else:
        rail_lengths = {x: num_cycles * 2 for x in range(2, n)}
        rail_lengths[1] = num_cycles
        rail_lengths[n] = num_cycles """

    print(f"rail lengths {rail_lengths}")

    encoded_iter = iter(encoded)
    return (''.join(islice(encoded_iter, rail_lengths[k]))
            for k in sorted(rail_lengths))


def encode_rail_fence_cipher(string, n):
    print(f"encoding {string} with {n} rails")
    rail_num = rail_sequence(n)

    rails = defaultdict(str)
    for char in string:
        rail = next(rail_num)
        # print(f"putting {char} in rail {rail}")
        rails[rail] += char

    encoded = ''.join(rails.values())
    print(f"encoded {encoded}")
    return encoded


def decode_rail_fence_cipher(string, n):
    print(f"\ndecoding <{string}> on {n} rails")
    """
    2 -> 1,1    1/2
    3 -> 1,2,1  1/4, 2/4
    4 -> 1,2,2,1 1/6, 2/6
    5 -> 1,2,2,2,1 1/8, 2/8
    n -> 1,2,2,..,n   1/(n-1)*2   2/(n-1)*2
    
    break string into n sections. rail 1 - 1/s   rail n - 1/s  everything else 2/s
    
    "abcdefgh", 3       -> "aebdfhcg"           1, 3, 7, 4, 2, 5, 8, 6
    "abcdefghijkl", 4   -> "agbfhlceikdj"       1, 3, 7, 11, 8, 4, 2, 5, 9, 12, 10, 6    
    """
    """ num_chunks = (
        n - 1) * 2  # 2 rails -> 1+1, 3 rails has 1+2+1, 4 has 1+2+2+1
    string_len = len(string)
    over = string_len % num_chunks """
    # if over:
    #    return 'dunno'
    # truncate to full string
    # string = string[0:-over]
    """ print(f"now string is <{string}> len={len(string)}. "
          f"Was len={string_len}, over {over}") """
    """
    pad_char = chr(22)
    pad_num = num_chunks - (string_len % num_chunks)
    print(f"need to pad with {pad} extras")
    string += pad_char * pad_num """
    """ string_len = len(string)  # Now have an evenly distributed string
    chunk_size = string_len // num_chunks
    print(f"string len {string_len} num_chunks {num_chunks} len {chunk_size}") """
    """ rails = {}
    string_iter = iter(string)
    for rail_num in range(1, n + 1):
        if rail_num == 1 or rail_num == n:
            chars_on_rail = chunk_size
        else:
            chars_on_rail = chunk_size * 2

        rails[rail_num] = next_chars(chars_on_rail, string_iter) """

    rails = [''] + [r for r in split_rails(string, n)]
    print(f"rails {rails}")
    rail_iter = [iter(rails[r]) for r in range(1, n + 1)]
    # print(f"rail iter {rail_iter}")

    decode = ''
    rail_num = rail_sequence(n)
    try:
        for rn in rail_num:
            print(f"rn {rn}")
            decode += next(rail_iter[rn - 1])
            print(f"decode now {decode}")
    except StopIteration:
        pass
    print(f"think it decodes to {decode}")
    return decode
    """
    h     .      !          2 + 1
     e   ,  W   d           4 (could have been +2)
      l o    o l            4 (could have been +2)
       l      r             2 (could have been +1)
       
    
       
    """

    #rails[n] = string[-chunk_size:]

    print(f"rails {rails}")

    rail = 1
    rail_inc = 1

    for char in string:
        rails[rail] += char

        if not 1 <= (rail + rail_inc) <= n:
            rail_inc *= -1
        rail += rail_inc

    return ''.join(rails.values())


"""
import string
orig = string.ascii_lowercase
code = encode_rail_fence_cipher(orig, 5)
while orig != code:
    print(f"code {code}")
    code = encode_rail_fence_cipher(code, 5) """

# Encode
""" assert encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE",
                                3) == "WECRLTEERDSOEEFEAOCAIVDEN"
assert encode_rail_fence_cipher("abcdefgh", 3) == "aebdfhcg"  # even chunks
assert encode_rail_fence_cipher("abcdefghi", 3) == "aeibdfhcg"  # 1 extra
assert encode_rail_fence_cipher("abcdefghij", 3) == "aeibdfhjcg"  # 2 extra
assert encode_rail_fence_cipher("abcdefghijk", 3) == "aeibdfhjcgk"  # 3 extra
assert encode_rail_fence_cipher("abcdefghijkl",
                                3) == "aeibdfhjlcgk"  # 4 extra back to even
assert encode_rail_fence_cipher("abcdefghijkl", 4) == "agbfhlceikdj"
assert encode_rail_fence_cipher("Hello, World!", 3) == "Hoo!el,Wrdl l"
assert encode_rail_fence_cipher("Hello,.World!", 4) == "H.!e,Wdloollr"
assert encode_rail_fence_cipher("Hello,.World", 4) == "H.e,Wdloollr"
assert encode_rail_fence_cipher("", 3) == "" """
# Decode
assert decode_rail_fence_cipher("H.e,Wdloollr", 4) == "Hello,.World"
assert decode_rail_fence_cipher("H !e,Wdloollr", 4) == "Hello, World!"
assert decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN",
                                3) == "WEAREDISCOVEREDFLEEATONCE"
assert decode_rail_fence_cipher("", 3) == ""
"""

"abcdefgh",     3) == "aebdfhcg"        # even chunks
"abcdefghi",    3) == "aeibdfhcg"       # 1 extra
"abcdefghij",   3) == "aeibdfhjcg"      # 2 extra
"abcdefghijk",  3) == "aeibdfhjcgk"     # 3 extra
"abcdefghijkl", 3) == "aeibdfhjlcgk"    # 4 extra bvack to even

"""