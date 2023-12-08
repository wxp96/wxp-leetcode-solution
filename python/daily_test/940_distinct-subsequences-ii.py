from ast import Mod


MOD=10**9+7
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        f=[0]*26
        for i,ch in enumerate(s):
            ch=ord(ch)-ord('a')
            f[ch]=(1+sum(f))%MOD
        return sum(f)%MOD