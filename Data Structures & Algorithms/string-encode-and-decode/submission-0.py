class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for st in strs:
            encoded_str += st + "\n"
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = list(s.split("\n"))
        print(decoded_str)
        return decoded_str[:-1]
