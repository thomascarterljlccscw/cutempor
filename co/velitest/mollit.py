def extract_vectors(string):
    vectors = string.split(',')
    vectors = [vector.strip() for vector in vectors]
    return vectors
