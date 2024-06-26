import heapq
from collections import Counter, defaultdict

# Run Length Encoding (RLE)
def run_length_encoding(data):
    encoded_data = []
    i = 0
    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            count += 1
            i += 1
        encoded_data.append((data[i], count))
        i += 1
    return encoded_data

# Huffman Encoding
def huffman_encoding(data):
    freq = Counter(data)
    heap = [[weight, [symbol, '']] for symbol, weight in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    codes = dict(heapq.heappop(heap)[1:])
    encoded_data = ''.join([codes[symbol] for symbol in data])
    return encoded_data, codes

# Lempel-Ziv (LZ) Encoding
def lz_encoding(data):
    dictionary = {}
    encoded_data = []
    idx = 256
    w = ''
    for c in data:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            encoded_data.append(dictionary.get(w, 0))
            dictionary[wc] = idx
            idx += 1
            w = c
    encoded_data.append(dictionary.get(w, 0))
    return encoded_data, dictionary

# Shannon-Fano Algorithm
def shannon_fano_encoding(data):
    def shannon_fano_rec(freq, start, end):
        if start >= end:
            return
        mid = (start + end) // 2
        for i in range(start, mid + 1):
            codes[i] += '0'
        for i in range(mid + 1, end + 1):
            codes[i] += '1'
        shannon_fano_rec(freq, start, mid)
        shannon_fano_rec(freq, mid + 1, end)

    freq = Counter(data)
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    codes = defaultdict(str)
    shannon_fano_rec(sorted_freq, 0, len(sorted_freq) - 1)
    encoded_data = ''.join([codes[symbol] for symbol in data])
    return encoded_data, dict(codes)

# Test the functions
data = "abracadabra"

# Run Length Encoding
rle_encoded_data = run_length_encoding(data)
print("Run Length Encoded Data:", rle_encoded_data)

# Huffman Encoding
huffman_encoded_data, huffman_codes = huffman_encoding(data)
print("Huffman Encoded Data:", huffman_encoded_data)
print("Huffman Codes:", huffman_codes)

# Lempel-Ziv (LZ) Encoding
lz_encoded_data, lz_dictionary = lz_encoding(data)
print("Lempel-Ziv Encoded Data:", lz_encoded_data)
print("Lempel-Ziv Dictionary:", lz_dictionary)

# Shannon-Fano Algorithm
shannon_fano_encoded_data, shannon_fano_codes = shannon_fano_encoding(data)
print("Shannon-Fano Encoded Data:", shannon_fano_encoded_data)
print("Shannon-Fano Codes:", shannon_fano_codes)