from raw import fasta_alignment


def main():
    query = "AGCTGACGTAG"
    target = "CGTAGAGCTGAC"
    k = 4

    score, alignment, aligned_q, aligned_t = fasta_alignment(query, target, k)

    print("Score:", score)
    print("Alignment starts at:", alignment)
    print("Query:", aligned_q)
    print("Target:", aligned_t)


if __name__ == "__main__":
    main()