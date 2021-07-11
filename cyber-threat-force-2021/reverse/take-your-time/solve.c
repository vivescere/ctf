#include <stdio.h>
#include <stdlib.h>

unsigned int fibo(unsigned int param) {
	if (param == 50) return 12586269025;
    if (param == 51) return 20365011074;
    if (param == 52) return 32951280099;
    if (param == 53) return 53316291173;
    if (param == 54) return 86267571272;
    if (param == 55) return 139583862445;
    if (param == 56) return 225851433717;
    if (param == 57) return 365435296162;
    if (param == 58) return 591286729879;
    if (param == 59) return 956722026041;
    if (param == 60) return 1548008755920;
    if (param == 61) return 2504730781961;
    if (param == 62) return 4052739537881;
    if (param == 63) return 6557470319842;
    if (param == 64) return 10610209857723;
    if (param == 65) return 17167680177565;
    if (param == 66) return 27777890035288;
    if (param == 67) return 44945570212853;
    if (param == 68) return 72723460248141;
    if (param == 69) return 117669030460994;
    if (param == 70) return 190392490709135;
    if (param == 71) return 308061521170129;
    if (param == 72) return 498454011879264;
    if (param == 73) return 806515533049393;
    if (param == 74) return 1304969544928657;
    if (param == 75) return 2111485077978050;
    if (param == 76) return 3416454622906707;
    if (param == 77) return 5527939700884757;
    if (param == 78) return 8944394323791464;
    return -1;
}

int main(void) {
	unsigned int FLAG[] = {
		0xb5,
		0x63,
		0x98,
		0x3d,
		0xb5,
		0x06,
		0x46,
		0xba,
		0x0f,
		0xd5,
		0x47,
		0xce,
		0x97,
		0xef,
		0x7b,
		0x28,
		0xdb,
		0xe7,
		0x39,
		0x10,
		0xb0,
		0xf5,
		0x44,
		0xec,
		0x30,
		0x88,
		0x46,
		0xf6,
		0x88,
	};

	unsigned int seed = 0;

	for (unsigned int i = 0x32; i < 0x4f; i++) {
		unsigned int res = fibo(i);
		seed = seed >> 8 | (seed ^ res) << 0x18;
	}

	srand(seed);

	for (unsigned int i2 = 0; i2 < 0x1d; i2++) {
		unsigned int res = FLAG[i2];
		putchar((unsigned int) res ^ rand() % 0xff);
	}

	puts("\n");
	return 0;
}

