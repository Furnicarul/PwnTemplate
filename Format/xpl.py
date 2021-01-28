from pwn import *
#context_level='DEBUG'

p = process("./format")
elf = ELF("./format", checksec=False)

def main():

	p.interactive()

if __name__=="__main__":
	main()
