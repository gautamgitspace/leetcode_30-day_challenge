bool isPowerOfTwo(int n){
    if (n ==0 || n < 0){
        return false;
    }
    unsigned int count = 0;
    while (n) {
        count += n & 1;
        n >>= 1;
    }
    if (count == 1) { return true; }
    return false;
}
