# EM enumeration definitions
EM_NONE = 0
EM_M32 = 1
EM_SPARC = 2
EM_386 = 3
EM_68K = 4
EM_88K = 5
EM_860 = 7
EM_MIPS = 8
EM_S370 = 9
EM_MIPS_RS3_LE = 10
EM_PARISC = 15
EM_VPP500 = 17
EM_SPARC32PLUS = 18
EM_960 = 19
EM_PPC = 20
EM_PPC64 = 21
EM_S390 = 22
EM_V800 = 36
EM_FR20 = 37
EM_RH32 = 38
EM_RCE = 39
EM_ARM = 40
EM_FAKE_ALPHA = 41
EM_SH = 42
EM_SPARCV9 = 43
EM_TRICORE = 44
EM_ARC = 45
EM_H8_300 = 46
EM_H8_300H = 47
EM_H8S = 48
EM_H8_500 = 49
EM_IA_64 = 50
EM_MIPS_X = 51
EM_COLDFIRE = 52
EM_68HC12 = 53
EM_MMA = 54
EM_PCP = 55
EM_NCPU = 56
EM_NDR1 = 57
EM_STARCORE = 58
EM_ME16 = 59
EM_ST100 = 60
EM_TINYJ = 61
EM_X86_64 = 62
EM_PDSP = 63
EM_FX66 = 66
EM_ST9PLUS = 67
EM_ST7 = 68
EM_68HC16 = 69
EM_68HC11 = 70
EM_68HC08 = 71
EM_68HC05 = 72
EM_SVX = 73
EM_ST19 = 74
EM_VAX = 75
EM_CRIS = 76
EM_JAVELIN = 77
EM_FIREPATH = 78
EM_ZSP = 79
EM_MMIX = 80
EM_HUANY = 81
EM_PRISM = 82
EM_AVR = 83
EM_FR30 = 84
EM_D10V = 85
EM_D30V = 86
EM_V850 = 87
EM_M32R = 88
EM_MN10300 = 89
EM_MN10200 = 90
EM_PJ = 91
EM_OPENRISC = 92
EM_ARC_A5 = 93
EM_XTENSA = 94
EM_NUM = 95
EM_MSP430 = 105
EM_ARM_AARCH64 = 183
EM_ALPHA = 0x9026

# There are plenty more of these to
# fill in, but...  this is all I need
# for now...
e_machine_32 = (
    EM_386,
    EM_PPC,
    EM_ARM,
)

e_machine_64 = (
    EM_PPC64,
    EM_SPARCV9,
    EM_X86_64,
    EM_ARM_AARCH64,
)

ELFCLASSNONE = 0
ELFCLASS32 = 1  # 32-bit object file
ELFCLASS64 = 2  # 64-bit object file

ELFDATANONE = 0
ELFDATA2LSB = 1
ELFDATA2MSB = 2

e_machine_types = {
    EM_NONE: "No machine",
    EM_M32: "AT&T WE 32100",
    EM_SPARC: "SUN SPARC",
    EM_386: "Intel 80386",
    EM_68K: "Motorola m68k family",
    EM_88K: "Motorola m88k family",
    EM_860: "Intel 80860",
    EM_MIPS: "MIPS R3000 big-endian",
    EM_S370: "IBM System/370",
    EM_MIPS_RS3_LE: "MIPS R3000 little-endian",
    EM_PARISC: "HPPA",
    EM_VPP500: "Fujitsu VPP500",
    EM_SPARC32PLUS: "Suns v8plus",
    EM_960: "Intel 80960",
    EM_PPC: "PowerPC",
    EM_PPC64: "PowerPC 64-bit",
    EM_S390: "IBM S390",
    EM_V800: "NEC V800 series",
    EM_FR20: "Fujitsu FR20",
    EM_RH32: "TRW RH-32",
    EM_RCE: "Motorola RCE",
    EM_ARM: "ARM",
    EM_FAKE_ALPHA: "Digital Alpha",
    EM_SH: "Hitachi SH",
    EM_SPARCV9: "SPARC v9 64-bit",
    EM_TRICORE: "Siemens Tricore",
    EM_ARC: "Argonaut RISC Core",
    EM_H8_300: "Hitachi H8/300",
    EM_H8_300H: "Hitachi H8/300H",
    EM_H8S: "Hitachi H8S",
    EM_H8_500: "Hitachi H8/500",
    EM_IA_64: "Intel Merced",
    EM_MIPS_X: "Stanford MIPS-X",
    EM_COLDFIRE: "Motorola Coldfire",
    EM_68HC12: "Motorola M68HC12",
    EM_MMA: "Fujitsu MMA Multimedia",
    EM_PCP: "Siemens PCP",
    EM_NCPU: "Sony nCPU embeeded RISC",
    EM_NDR1: "Denso NDR1 microprocessor",
    EM_STARCORE: "Motorola Start*Core processor",
    EM_ME16: "Toyota ME16 processor",
    EM_ST100: "STMicroelectronic ST100 processor",
    EM_TINYJ: "Advanced Logic Corp. Tinyj",
    EM_X86_64: "AMD x86-64 architecture",
    EM_PDSP: "Sony DSP Processor",
    EM_FX66: "Siemens FX66 microcontroller",
    EM_ST9PLUS: "STMicroelectronics ST9+ 8/16 mc",
    EM_ST7: "STmicroelectronics ST7 8 bit mc",
    EM_68HC16: "Motorola MC68HC16 microcontroller",
    EM_68HC11: "Motorola MC68HC11 microcontroller",
    EM_68HC08: "Motorola MC68HC08 microcontroller",
    EM_68HC05: "Motorola MC68HC05 microcontroller",
    EM_SVX: "Silicon Graphics SVx",
    EM_ST19: "STMicroelectronics ST19 8 bit mc",
    EM_VAX: "Digital VAX",
    EM_CRIS: "Axis Communications 32-bit embedded processor",
    EM_JAVELIN: "Infineon Technologies 32-bit embedded processor",
    EM_FIREPATH: "Element 14 64-bit DSP Processor",
    EM_ZSP: "LSI Logic 16-bit DSP Processor",
    EM_MMIX: "Donald Knuths educational 64-bit processor",
    EM_HUANY: "Harvard University machine-independent object files",
    EM_PRISM: "SiTera Prism",
    EM_AVR: "Atmel AVR 8-bit microcontroller",
    EM_FR30: "Fujitsu FR30",
    EM_D10V: "Mitsubishi D10V",
    EM_D30V: "Mitsubishi D30V",
    EM_V850: "NEC v850",
    EM_M32R: "Mitsubishi M32R",
    EM_MN10300: "Matsushita MN10300",
    EM_MN10200: "Matsushita MN10200",
    EM_PJ: "picoJava",
    EM_OPENRISC: "OpenRISC 32-bit embedded processor",
    EM_ARC_A5: "ARC Cores Tangent-A5",
    EM_XTENSA: "Tensilica Xtensa Architecture",
    EM_NUM: "",
    EM_ARM_AARCH64: "ARM aarch64",
    EM_ALPHA: "",
}

ET_NONE = 0
ET_REL = 1
ET_EXEC = 2
ET_DYN = 3
ET_CORE = 4
ET_NUM = 5
ET_LOOS = 0xfe00
ET_HIOS = 0xfeff
ET_LOPROC = 0xff00
ET_HIPROC = 0xffff

e_types = {
    ET_NONE: "No file type",
    ET_REL: "Relocatable file",
    ET_EXEC: "Executable file",
    ET_DYN: "Shared object file",
    ET_CORE: "Core file",
    ET_NUM: "Number of defined types",
    ET_LOOS: "OS-specific range start",
    ET_HIOS: "OS-specific range end",
    ET_LOPROC: "Processor-specific range start",
    ET_HIPROC: "Processor-specific range end",
}

EV_NONE = 0
EV_CURRENT = 1
EV_NUM = 2

e_versions = {
    EV_NONE: "Invalid ELF version",
    EV_CURRENT: "Current version",
    EV_NUM: "",
}

R_68K_NONE = 0
R_68K_32 = 1
R_68K_16 = 2
R_68K_8 = 3
R_68K_PC32 = 4
R_68K_PC16 = 5
R_68K_PC8 = 6
R_68K_GOT32 = 7
R_68K_GOT16 = 8
R_68K_GOT8 = 9
R_68K_GOT32O = 10
R_68K_GOT16O = 11
R_68K_GOT8O = 12
R_68K_PLT32 = 13
R_68K_PLT16 = 14
R_68K_PLT8 = 15
R_68K_PLT32O = 16
R_68K_PLT16O = 17
R_68K_PLT8O = 18
R_68K_COPY = 19
R_68K_GLOB_DAT = 20
R_68K_JMP_SLOT = 21
R_68K_RELATIVE = 22

e_flags_68k = {
    R_68K_NONE: "No reloc",
    R_68K_32: "Direct 32 bit",
    R_68K_16: "Direct 16 bit",
    R_68K_8: "Direct 8 bit",
    R_68K_PC32: "PC relative 32 bit",
    R_68K_PC16: "PC relative 16 bit",
    R_68K_PC8: "PC relative 8 bit",
    R_68K_GOT32: "32 bit PC relative GOT entry",
    R_68K_GOT16: "16 bit PC relative GOT entry",
    R_68K_GOT8: "8 bit PC relative GOT entry",
    R_68K_GOT32O: "32 bit GOT offset",
    R_68K_GOT16O: "16 bit GOT offset",
    R_68K_GOT8O: "8 bit GOT offset",
    R_68K_PLT32: "32 bit PC relative PLT address",
    R_68K_PLT16: "16 bit PC relative PLT address",
    R_68K_PLT8: "8 bit PC relative PLT address",
    R_68K_PLT32O: "32 bit PLT offset",
    R_68K_PLT16O: "16 bit PLT offset",
    R_68K_PLT8O: "8 bit PLT offset",
    R_68K_COPY: "Copy symbol at runtime",
    R_68K_GLOB_DAT: "Create GOT entry",
    R_68K_JMP_SLOT: "Create PLT entry",
    R_68K_RELATIVE: "Adjust by program base",
}

R_ARM_NONE          = 0   # No reloc */
R_ARM_PC24          = 1   # PC relative 26 bit branch */
R_ARM_ABS32         = 2   # Direct 32 bit  */
R_ARM_REL32         = 3   # PC relative 32 bit */
R_ARM_PC13          = 4
R_ARM_LDR_PC_G0     = 4   # also 4
R_ARM_ABS16         = 5   # Direct 16 bit */
R_ARM_ABS12         = 6   # Direct 12 bit */
R_ARM_THM_ABS5      = 7
R_ARM_ABS8          = 8   # Direct 8 bit */
R_ARM_SBREL32       = 9
R_ARM_THM_PC22      = 10
R_ARM_THM_PC8       = 11
R_ARM_AMP_VCALL9    = 12
R_ARM_BREL_ADJ      = 12  # also 12
R_ARM_SWI24         = 13
R_ARM_TLS_DESC      = 13  # also 13
R_ARM_THM_SWI8      = 14
R_ARM_XPC25         = 15
R_ARM_THM_XPC22     = 16
R_ARM_TLS_DTPMOD32  = 17  # ID of module containing symbol */
R_ARM_TLS_DTPOFF32  = 18  # Offset in TLS block */
R_ARM_TLS_TPOFF32   = 19  # Offset in static TLS block */
R_ARM_COPY          = 20  # Copy symbol at runtime */
R_ARM_GLOB_DAT      = 21  # Create GOT entry */
R_ARM_JUMP_SLOT     = 22  # Create PLT entry */
R_ARM_RELATIVE      = 23  # Adjust by program base */
R_ARM_GOTOFF        = 24  # 32 bit offset to GOT */
R_ARM_GOTPC         = 25  # 32 bit PC relative offset to GOT */
R_ARM_GOT32         = 26  # 32 bit GOT entry */
R_ARM_PLT32         = 27  # 32 bit PLT address */
R_ARM_CALL          = 28
R_ARM_JUMP24        = 29
R_ARM_THM_JUMP24        = 30
R_ARM_BASE_ABS          = 31
R_ARM_ALU_PCREL_7_0     = 32
R_ARM_ALU_PCREL_15_8    = 33
R_ARM_ALU_PCREL_23_15   = 34
R_ARM_LDR_SBREL_11_0    = 35
R_ARM_ALU_SBREL_19_12   = 36
R_ARM_ALU_SBREL_27_20   = 37
R_ARM_GNU_VTENTRY   = 100
R_ARM_GNU_VTINHERIT = 101
R_ARM_THM_PC11      = 102 # thumb unconditional branch */
R_ARM_THM_PC9       = 103 # thumb conditional branch */
R_ARM_TLS_GD32      = 104 # PC-rel 32 bit for global dynamic thread local data */
R_ARM_TLS_LDM32     = 105 # PC-rel 32 bit for local dynamic thread local data */
R_ARM_TLS_LDO32     = 106 # 32 bit offset relative to TLS block */
R_ARM_TLS_IE32      = 107 # PC-rel 32 bit for GOT entry of static TLS block offset */
R_ARM_TLS_LE32      = 108 # 32 bit offset relative to static TLS block */
R_ARM_IRELATIVE     = 160
R_ARM_RXPC25        = 249
R_ARM_RSBREL32      = 250
R_ARM_THM_RPC22     = 251
R_ARM_RREL32        = 252
R_ARM_RABS22        = 253
R_ARM_RPC24         = 254
R_ARM_RBASE         = 255

R_ARMCLASS_DATA = 0
R_ARMCLASS_ARM = 1
R_ARMCLASS_THUMB16 = 2
R_ARMCLASS_THUMB32 = 3
R_ARMCLASS_MISC = 4

r_armclasses = [
        (R_ARM_ABS32,
            R_ARM_REL32,
            R_ARM_ABS16,
            R_ARM_ABS8,
            R_ARM_SBREL32,
            R_ARM_BREL_ADJ,
            R_ARM_TLS_DESC,
            R_ARM_TLS_DTPMOD32,
            R_ARM_TLS_DTPOFF32,
            R_ARM_TLS_TPOFF32,
            R_ARM_GLOB_DAT,
            R_ARM_JUMP_SLOT,
            R_ARM_RELATIVE,
            R_ARM_GOTOFF,
            R_ARM_GOTPC,
            R_ARM_GOT32,
            R_ARM_IRELATIVE,
            ),
        (
            R_ARM_PC24,
            R_ARM_LDR_PC_G0,
            R_ARM_ABS12,
            R_ARM_PLT32,
            R_ARM_CALL,
            R_ARM_JUMP24,
            R_ARM_LDR_SBREL_11_0,
            R_ARM_ALU_SBREL_19_12,
            R_ARM_ALU_SBREL_27_20,
            ),
        (
            R_ARM_THM_ABS5,
            R_ARM_THM_PC8,
            ),
        (
            R_ARM_THM_PC22,
            R_ARM_THM_JUMP24,
            ),
        (
            R_ARM_NONE,
            R_ARM_COPY,
            ),
        ]








R_386_NONE = 0
R_386_32 = 1
R_386_PC32 = 2
R_386_GOT32 = 3
R_386_PLT32 = 4
R_386_COPY = 5
R_386_GLOB_DAT = 6
R_386_JMP_SLOT = 7
R_386_RELATIVE = 8
R_386_GOTOFF = 9
R_386_GOTPC = 10
R_386_32PLT = 11
R_386_TLS_TPOFF = 14
R_386_TLS_IE = 15
R_386_TLS_GOTIE = 16
R_386_TLS_LE = 17
R_386_TLS_GD = 18
R_386_TLS_LDM = 19
R_386_16 = 20
R_386_PC16 = 21
R_386_8 = 22
R_386_PC8 = 23
R_386_TLS_GD_32 = 24
R_386_TLS_GD_PUSH = 25
R_386_TLS_GD_CALL = 26
R_386_TLS_GD_POP = 27
R_386_TLS_LDM_32 = 28
R_386_TLS_LDM_PUSH = 29
R_386_TLS_LDM_CALL = 30
R_386_TLS_LDM_POP = 31
R_386_TLS_LDO_32 = 32
R_386_TLS_IE_32 = 33
R_386_TLS_LE_32 = 34
R_386_TLS_DTPMOD32 = 35
R_386_TLS_DTPOFF32 = 36
R_386_TLS_TPOFF32 = 37

r_types_386 = {
    R_386_NONE: "No reloc",
    R_386_32: "Direct 32 bit",
    R_386_PC32: "PC relative 32 bit",
    R_386_GOT32: "32 bit GOT entry",
    R_386_PLT32: "32 bit PLT address",
    R_386_COPY: "Copy symbol at runtime",
    R_386_GLOB_DAT: "Create GOT entry",
    R_386_JMP_SLOT: "Create PLT entry",
    R_386_RELATIVE: "Adjust by program base",
    R_386_GOTOFF: "32 bit offset to GOT",
    R_386_GOTPC: "32 bit PC relative offset to GOT",
    R_386_32PLT: "",
    R_386_TLS_TPOFF: "Offset in static TLS block",
    R_386_TLS_IE: "Address of GOT entry for static",
    R_386_TLS_GOTIE: "GOT entry for static TLS",
    R_386_TLS_LE: "Offset relative to static",
    R_386_TLS_GD: "Direct 32 bit for GNU version",
    R_386_TLS_LDM: "Direct 32 bit for GNU version",
    R_386_16: "",
    R_386_PC16: "",
    R_386_8: "",
    R_386_PC8: "",
    R_386_TLS_GD_32: "Direct 32 bit for general",
    R_386_TLS_GD_PUSH: "Tag for pushl in GD TLS code",
    R_386_TLS_GD_CALL: "Relocation for call",
    R_386_TLS_GD_POP: "Tag for popl in GD TLS code",
    R_386_TLS_LDM_32: "Direct 32 bit for local",
    R_386_TLS_LDM_PUSH: "Tag for pushl in LDM TLS code",
    R_386_TLS_LDM_CALL: "Relocation for call",
    R_386_TLS_LDM_POP: "Tag for popl in LDM TLS code",
    R_386_TLS_LDO_32: "Offset relative to TLS block",
    R_386_TLS_IE_32: "GOT entry for negated static",
    R_386_TLS_LE_32: "Negated offset relative to",
    R_386_TLS_DTPMOD32: "ID of module containing symbol",
    R_386_TLS_DTPOFF32: "Offset in TLS block",
    R_386_TLS_TPOFF32: "Negated offset in static TLS block",
}

R_X86_64_NONE = 0
R_X86_64_64 = 1
R_X86_64_PC32 = 2
R_X86_64_GOT32 = 3
R_X86_64_PLT32 = 4
R_X86_64_COPY = 5
R_X86_64_GLOB_DAT = 6
R_X86_64_JUMP_SLOT = 7
R_X86_64_RELATIVE = 8
R_X86_64_GOTPCREL = 9
R_X86_64_32 = 10
R_X86_64_32S = 11
R_X86_64_16 = 12
R_X86_64_PC16 = 13
R_X86_64_8 = 14
R_X86_64_PC8 = 15
R_X86_64_DTPMOD64 = 16
R_X86_64_DTPOFF64 = 17
R_X86_64_TPOFF64 = 18
R_X86_64_TLSGD = 19
R_X86_64_TLSLD = 20
R_X86_64_DTPOFF32 = 21
R_X86_64_GOTTPOFF = 22
R_X86_64_TPOFF32 = 23
R_X86_64_NUM = 24
R_X86_64_GOTOFF64 = 25
R_X86_64_GOTPC32 = 26
R_X86_64_GOT64 = 27
R_X86_64_GOTPCREL64 = 28
R_X86_64_GOTPC64 = 29
R_X86_64_GOTPLT64 = 30
R_X86_64_PLTOFF64 = 31
R_X86_64_SIZE32 = 32
R_X86_64_SIZE64 = 33
R_X86_64_GOTPC32_TLSDESC = 34
R_X86_64_TLSDESC_CALL = 35
R_X86_64_TLSDESC = 36
R_X86_64_IRELATIVE = 37

r_types_amd64 = {
    R_X86_64_NONE: 'No reloc',
    R_X86_64_64: 'Direct 64 bit ',
    R_X86_64_PC32: 'PC relative 32 bit signed',
    R_X86_64_GOT32: '32 bit GOT entry',
    R_X86_64_PLT32: '32 bit PLT address',
    R_X86_64_COPY: 'Copy symbol at runtime',
    R_X86_64_GLOB_DAT: 'Create GOT entry',
    R_X86_64_JUMP_SLOT: 'Create PLT entry',
    R_X86_64_RELATIVE: 'Adjust by program base',
    R_X86_64_GOTPCREL: '32 bit signed PC relative offset to GOT',
    R_X86_64_32: 'Direct 32 bit zero extended',
    R_X86_64_32S: 'Direct 32 bit sign extended',
    R_X86_64_16: 'Direct 16 bit zero extended',
    R_X86_64_PC16: '16 bit sign extended pc relative',
    R_X86_64_8: 'Direct 8 bit sign extended ',
    R_X86_64_PC8: '8 bit sign extended pc relative',
    R_X86_64_DTPMOD64: 'ID of module containing symbol',
    R_X86_64_DTPOFF64: 'Offset in modules TLS block',
    R_X86_64_TPOFF64: 'Offset in initial TLS block',
    R_X86_64_TLSGD: '32 bit signed PC relative offset to two GOT entries for GD symbol',
    R_X86_64_TLSLD: '32 bit signed PC relative offset to two GOT entries for LD symbol',
    R_X86_64_DTPOFF32: 'Offset in TLS block',
    R_X86_64_GOTTPOFF: '32 bit signed PC relative offset to GOT entry for IE symbol',
    R_X86_64_TPOFF32: 'Offset in initial TLS block',
    R_X86_64_GOTOFF64: '64 bit offset to GOT',
    R_X86_64_GOTPC32: '32 bit signed pc relative offset to GOT',
    R_X86_64_GOT64: '64-bit GOT entry offset',
    R_X86_64_GOTPCREL64: '64-bit PC relative offset to GOT entry',
    R_X86_64_GOTPC64: '64-bit PC relative offset to GOT',
    R_X86_64_GOTPLT64: 'like GOT64, says PLT entry needed',
    R_X86_64_PLTOFF64: '64-bit GOT relative offset to PLT entry',
    R_X86_64_SIZE32: 'Size of symbol plus 32-bit addend',
    R_X86_64_SIZE64: 'Size of symbol plus 64-bit addend',
    R_X86_64_GOTPC32_TLSDESC: 'GOT offset for TLS descriptor.',
    R_X86_64_TLSDESC_CALL: 'Marker for call through TLS descriptor.',
    R_X86_64_TLSDESC: 'TLS descriptor.',
    R_X86_64_IRELATIVE: 'Adjust indirectly by program base',
}

# Define e_flags to 386
SHT_NULL = 0
SHT_PROGBITS = 1
SHT_SYMTAB = 2
SHT_STRTAB = 3
SHT_RELA = 4
SHT_HASH = 5
SHT_DYNAMIC = 6
SHT_NOTE = 7
SHT_NOBITS = 8
SHT_REL = 9
SHT_SHLIB = 10
SHT_DYNSYM = 11
SHT_INIT_ARRAY = 14
SHT_FINI_ARRAY = 15
SHT_PREINIT_ARRAY = 16
SHT_GROUP = 17
SHT_SYMTAB_SHNDX = 18
SHT_LOOS = 0x60000000
SHT_GNU_LIBLIST = 0x6ffffff7
SHT_CHECKSUM = 0x6ffffff8
SHT_LOSUNW = 0x6ffffffa
SHT_GNU_verdef = 0x6ffffffd
SHT_GNU_verneed = 0x6ffffffe
SHT_GNU_versym = 0x6fffffff
SHT_HISUNW = 0x6fffffff
SHT_HIOS = 0x6fffffff
SHT_LOPROC = 0x70000000
SHT_HIPROC = 0x7fffffff
SHT_LOUSER = 0x80000000
SHT_HIUSER = 0x8fffffff

sht_lookup ={y: x for x, y in globals().items() if x.startswith("SHT_")}

sh_type = {
    SHT_NULL: "Section header table entry unused",
    SHT_PROGBITS: "Program data",
    SHT_SYMTAB: "Symbol table",
    SHT_STRTAB: "String table",
    SHT_RELA: "Relocation entries with addends",
    SHT_HASH: "Symbol hash table",
    SHT_DYNAMIC: "Dynamic linking information",
    SHT_NOTE: "Notes",
    SHT_NOBITS: "Program space with no data (bss)",
    SHT_REL: "Relocation entries, no addends",
    SHT_SHLIB: "Reserved",
    SHT_DYNSYM: "Dynamic linker symbol table",
    SHT_INIT_ARRAY: "Array of constructors",
    SHT_FINI_ARRAY: "Array of destructors",
    SHT_PREINIT_ARRAY: "Array of pre-constructors",
    SHT_GROUP: "Section group",
    SHT_SYMTAB_SHNDX: "Extended section indeces",
    SHT_LOOS: "Start OS-specific",
    SHT_GNU_LIBLIST: "Prelink library list",
    SHT_CHECKSUM: "Checksum for DSO content.",
    SHT_LOSUNW: "Sun-specific low bound.",
    SHT_GNU_verdef: "Version definition section.",
    SHT_GNU_verneed: "Version needs section.",
    SHT_GNU_versym: "Version symbol table.",
    SHT_HISUNW: "Sun-specific high bound.",
    SHT_HIOS: "End OS-specific type",
    SHT_LOPROC: "Start of processor-specific",
    SHT_HIPROC: "End of processor-specific",
    SHT_LOUSER: "Start of application-specific",
    SHT_HIUSER: "End of application-specific",
}

SHF_WRITE = 1
SHF_ALLOC = 2
SHF_EXECINSTR = 4
SHF_MERGE = 16
SHF_STRINGS = 32
SHF_INFO_LINK = 64
SHF_LINK_ORDER = 128
SHF_OS_NONCONFORMING = 256
SHF_GROUP = 512
SHF_TLS = 1024
SHF_ORDERED = 1073741824
SHF_EXCLUDE = 2147483648

sh_flags = {
    SHF_WRITE: "Writable",
    SHF_ALLOC: "Occupies memory during execution",
    SHF_EXECINSTR: "Executable",
    SHF_MERGE: "Might be merged",
    SHF_STRINGS: "Contains nul-terminated strings",
    SHF_INFO_LINK: "`sh_info' contains SHT index",
    SHF_LINK_ORDER: "Preserve order after combining",
    SHF_OS_NONCONFORMING: "Non-standard OS specific",
    SHF_GROUP: "Section is member of a group.",
    SHF_TLS: "Section hold thread-local data.",
    SHF_ORDERED: "Special ordering",
    SHF_EXCLUDE: "Section is excluded",
}

STB_LOCAL = 0
STB_GLOBAL = 1
STB_WEAK = 2
STB_LOOS = 10
STB_HIOS = 12
STB_LOPROC = 13
STB_HIPROC = 15

stb_lookup ={y: x for x, y in globals().items() if x.startswith("STB_")}

st_info_bind = {
    STB_LOCAL: "Local symbol",
    STB_GLOBAL: "Global symbol",
    STB_WEAK: "Weak symbol",
    STB_LOOS: "Start of OS-specific",
    STB_HIOS: "End of OS-specific",
    STB_LOPROC: "Start of processor-specific",
    STB_HIPROC: "End of processor-specific",
}

STT_NOTYPE = 0
STT_OBJECT = 1
STT_FUNC = 2
STT_SECTION = 3
STT_FILE = 4
STT_COMMON = 5
STT_TLS = 6
STT_LOOS = 10
STT_MDOS = 11  # there's only one that isn't HI or LO...
STT_HIOS = 12
STT_LOPROC = 13
STT_MDPROC = 14
STT_HIPROC = 15

STT_GNU_IFUNC = 10

stt_lookup ={y: x for x, y in globals().items() if x.startswith("STT_")}

st_info_type = {
    STT_NOTYPE: "Symbol type is unspecified",
    STT_OBJECT: "Symbol is a data object",
    STT_FUNC: "Symbol is a code object",
    STT_SECTION: "Symbol associated with a section",
    STT_FILE: "Symbol's name is file name",
    STT_COMMON: "Symbol is a common data object",
    STT_TLS: "Symbol is thread-local data",
    STT_LOOS: "Start of OS-specific",
    STT_MDOS: "Middle of OS-specific",
    STT_HIOS: "End of OS-specific",
    STT_LOPROC: "Start of processor-specific",
    STT_MDPROC: "Middle of processor-specific",
    STT_HIPROC: "End of processor-specific",
}

STV_DEFAULT     = 0
STV_INTERNAL    = 1
STV_HIDDEN      = 2
STV_PROTECTED   = 3

stv_lookup ={y: x for x, y in globals().items() if x.startswith("STV_")}

st_other_visibility = {
    STV_DEFAULT:"Symbol visibility specified by binding type",
    STV_INTERNAL:"Symbol visibility is reserved",
    STV_HIDDEN:"Symbol is not visible to other objects",
    STV_PROTECTED:"Symbol is visible by other objects, but cannot be preempted"
}

DT_NULL = 0
DT_NEEDED = 1
DT_PLTRELSZ = 2
DT_PLTGOT = 3
DT_HASH = 4
DT_STRTAB = 5
DT_SYMTAB = 6
DT_RELA = 7
DT_RELASZ = 8
DT_RELAENT = 9
DT_STRSZ = 10
DT_SYMENT = 11
DT_INIT = 12
DT_FINI = 13
DT_SONAME = 14
DT_RPATH = 15
DT_SYMBOLIC = 16
DT_REL = 17
DT_RELSZ = 18
DT_RELENT = 19
DT_PLTREL = 20
DT_DEBUG = 21
DT_TEXTREL = 22
DT_JMPREL = 23
DT_BIND_NOW = 24
DT_INIT_ARRAY = 25
DT_FINI_ARRAY = 26
DT_INIT_ARRAYSZ = 27
DT_FINI_ARRAYSZ = 28
DT_RUNPATH = 29
DT_FLAGS = 30
DT_ENCODING = 32
DT_PREINIT_ARRAY = 32
DT_PREINIT_ARRAYSZ = 33
DT_NUM = 34
DT_GNU_PRELINKED = 0x6ffffdf5
DT_GNU_CONFLICTSZ = 0x6ffffdf6
DT_GNU_LIBLISTSZ = 0x6ffffdf7
DT_CHECKSUM = 0x6ffffdf8
DT_PLTPADSZ = 0x6ffffdf9
DT_MOVEENT = 0x6ffffdfa
DT_MOVESZ = 0x6ffffdfb
DT_FEATURE_1 = 0x6ffffdfc
DT_POSFLAG_1 = 0x6ffffdfd
DT_SYMINSZ = 0x6ffffdfe
DT_SYMINENT = 0x6ffffdff
DT_GNU_HASH = 0x6ffffef5
DT_TLSDESC_PLT = 0x6ffffef6
DT_TLSDESC_GOT = 0x6ffffef7
DT_GNU_CONFLICT = 0x6ffffef8
DT_GNU_LIBLIST = 0x6ffffef9
DT_CONFIG = 0x6ffffefa
DT_DEPAUDIT = 0x6ffffefb
DT_AUDIT = 0x6ffffefc
DT_PLTPAD = 0x6ffffefd
DT_MOVETAB = 0x6ffffefe
DT_SYMINFO = 0x6ffffeff
DT_VERSYM = 0x6ffffff0
DT_RELACOUNT = 0x6ffffff9
DT_RELCOUNT = 0x6ffffffa
DT_FLAGS_1 = 0x6ffffffb
DT_VERDEF = 0x6ffffffc
DT_VERDEFNUM = 0x6ffffffd
DT_VERNEED = 0x6ffffffe
DT_VERNEEDNUM = 0x6fffffff
DT_AUXILIARY = 0x7ffffffd
DT_FILTER = 0x7fffffff
DT_LOOS = 0x6000000d
DT_HIOS = 0x6ffff000
DT_LOPROC = 0x70000000
DT_HIPROC = 0x7fffffff
# DT_PROCNUM  = DT_MIPS_NUM

dt_names = { v:k for k,v in globals().items() if k.startswith('DT_')}

dt_types = {
    DT_NULL: "Marks end of dynamic section ",
    DT_NEEDED: "Name of needed library ",
    DT_PLTRELSZ: "Size in bytes of PLT relocs ",
    DT_PLTGOT: "Processor defined value ",
    DT_HASH: "Address of symbol hash table ",
    DT_STRTAB: "Address of string table ",
    DT_SYMTAB: "Address of symbol table ",
    DT_RELA: "Address of Rela relocs ",
    DT_RELASZ: "Total size of Rela relocs ",
    DT_RELAENT: "Size of one Rela reloc ",
    DT_STRSZ: "Size of string table ",
    DT_SYMENT: "Size of one symbol table entry ",
    DT_INIT: "Address of init function ",
    DT_FINI: "Address of termination function ",
    DT_SONAME: "Name of shared object ",
    DT_RPATH: "Library search path (deprecated) ",
    DT_SYMBOLIC: "Start symbol search here ",
    DT_REL: "Address of Rel relocs ",
    DT_RELSZ: "Total size of Rel relocs ",
    DT_RELENT: "Size of one Rel reloc ",
    DT_PLTREL: "Type of reloc in PLT ",
    DT_DEBUG: "For debugging; unspecified ",
    DT_TEXTREL: "Reloc might modify .text ",
    DT_JMPREL: "Address of PLT relocs ",
    DT_BIND_NOW: "Process relocations of object ",
    DT_INIT_ARRAY: "Array with addresses of init fct ",
    DT_FINI_ARRAY: "Array with addresses of fini fct ",
    DT_INIT_ARRAYSZ: "Size in bytes of DT_INIT_ARRAY ",
    DT_FINI_ARRAYSZ: "Size in bytes of DT_FINI_ARRAY ",
    DT_RUNPATH: "Library search path ",
    DT_FLAGS: "Flags for the object being loaded ",
    DT_ENCODING: "Start of encoded range ",
    DT_PREINIT_ARRAY: "Array with addresses of preinit fct",
    DT_PREINIT_ARRAYSZ: "size in bytes of DT_PREINIT_ARRAY ",
    DT_NUM: "Number used ",
    DT_LOOS: "Start of OS-specific ",
    DT_HIOS: "End of OS-specific ",
    DT_LOPROC: "Start of processor-specific ",
    DT_HIPROC: "End of processor-specific ",
    DT_VERDEF: "Version Definition Offset ",
    DT_VERDEFNUM: "Version Definition Structure Count ",
    DT_VERNEED: "Required Version Offset ",
    DT_VERNEEDNUM: "Required Version Structure Count ",
    DT_VERSYM: "Address of Version Section"
    # DT_PROCNUM  : "Most used by any processor ",
}

PT_NULL = 0
PT_LOAD = 1
PT_DYNAMIC = 2
PT_INTERP = 3
PT_NOTE = 4
PT_SHLIB = 5
PT_PHDR = 6
PT_TLS = 7
PT_NUM = 8
PT_LOOS = 0x60000000
PT_GNU_EH_FRAME = 0x6474e550
PT_GNU_STACK = 0x6474e551
PT_GNU_RELRO = 0x6474e552
PT_LOSUNW = 0x6ffffffa
PT_SUNWBSS = 0x6ffffffa
PT_SUNWSTACK = 0x6ffffffb
PT_HISUNW = 0x6fffffff
PT_HIOS = 0x6fffffff
PT_LOPROC = 0x70000000
PT_HIPROC = 0x7fffffff

ph_types = {
    PT_NULL: "Program header table entry unused",
    PT_LOAD: "Loadable program segment",
    PT_DYNAMIC: "Dynamic linking information",
    PT_INTERP: "Program interpreter",
    PT_NOTE: "Auxiliary information",
    PT_SHLIB: "Reserved",
    PT_PHDR: "Entry for header table itself",
    PT_TLS: "Thread-local storage segment",
    PT_NUM: "Number of defined types",
    PT_LOOS: "Start of OS-specific",
    PT_GNU_EH_FRAME: "GCC .eh_frame_hdr segment",
    PT_GNU_STACK: "Indicates stack executability",
    PT_GNU_RELRO: "Read-only after relocation",
    PT_SUNWBSS: "Sun Specific segment",
    PT_SUNWSTACK: "Stack segment",
    PT_HIOS: "End of OS-specific",
    PT_LOPROC: "Start of processor-specific",
    PT_HIPROC: "End of processor-specific"
}

# GNU .note.ABI-tag
osnotes = {
    0: 'linux',
    1: 'gnu',
    2: 'solaris',
    3: 'freebsd',
}

# DWARF Debugging info Enums

DW_CHILDREN_no = 0x0
DW_CHILDREN_yes = 0x1

# DWARF Tag Encodings
DW_TAG_array_type = 0x1
DW_TAG_class_type = 0x2
DW_TAG_entry_point = 0x3
DW_TAG_enumeration_type = 0x4
DW_TAG_formal_parameter = 0x5
DW_TAG_imported_declaration = 0x8
DW_TAG_label = 0xa
DW_TAG_lexical_block = 0xb
DW_TAG_member = 0xd
DW_TAG_pointer_type = 0xf
DW_TAG_reference_type = 0x10
DW_TAG_compile_unit = 0x11
DW_TAG_string_type = 0x12
DW_TAG_structure_type = 0x13
DW_TAG_subroutine_type = 0x15
DW_TAG_typedef = 0x16
DW_TAG_union_type = 0x17
DW_TAG_unspecified_parameters = 0x18
DW_TAG_variant = 0x19
DW_TAG_common_block = 0x1a
DW_TAG_common_inclusion = 0x1b
DW_TAG_inheritance = 0x1c
DW_TAG_inlined_subroutine = 0x1d
DW_TAG_module = 0x1e
DW_TAG_ptr_to_member_type = 0x1f
DW_TAG_set_type = 0x20
DW_TAG_subrange_type = 0x21
DW_TAG_with_stmt = 0x22
DW_TAG_access_declaration = 0x23
DW_TAG_base_type = 0x24
DW_TAG_catch_block = 0x25
DW_TAG_const_type = 0x26
DW_TAG_constant = 0x27
DW_TAG_enumerator = 0x28
DW_TAG_file_type = 0x29
DW_TAG_friend = 0x2a
DW_TAG_namelist = 0x2b
DW_TAG_namelist_item = 0x2c
DW_TAG_packed_type = 0x2d
DW_TAG_subprogram = 0x2e
DW_TAG_template_type_parameter = 0x2f
DW_TAG_template_value_parameter = 0x30
DW_TAG_thrown_type = 0x31
DW_TAG_try_block = 0x32
DW_TAG_variant_part = 0x33
DW_TAG_variable = 0x34
DW_TAG_volatile_type = 0x35
DW_TAG_dwarf_procedure = 0x36
DW_TAG_restrict_type = 0x37
DW_TAG_interface_type = 0x38
DW_TAG_namespace = 0x39
DW_TAG_imported_module = 0x3a
DW_TAG_unspecified_type = 0x3b
DW_TAG_partial_unit = 0x3c
DW_TAG_imported_unit = 0x3d
DW_TAG_condition = 0x3f
DW_TAG_shared_type = 0x40
DW_TAG_type_unit = 0x41  # V4
DW_TAG_rvalue_reference_type = 0x42  # V4
DW_TAG_template_alias = 0x43  # V4
DW_TAG_lo_user = 0x4080
DW_TAG_hi_user = 0xffff


# DWARF Attribute Encodings
DW_AT_sibling = 0x1
DW_AT_location = 0x2
DW_AT_name = 0x3
DW_AT_ordering = 0x9
DW_AT_byte_size = 0xb
DW_AT_bit_offset = 0xc
DW_AT_bit_size = 0xd
DW_AT_stmt_list = 0x10
DW_AT_low_pc = 0x11
DW_AT_high_pc = 0x12
DW_AT_language = 0x13
DW_AT_discr = 0x15
DW_AT_discr_value = 0x16
DW_AT_visibility = 0x17
DW_AT_import = 0x18
DW_AT_string_length = 0x19
DW_AT_common_reference = 0x1a
DW_AT_comp_dir = 0x1b
DW_AT_const_value = 0x1c
DW_AT_containing_type = 0x1d
DW_AT_default_value = 0x1e
DW_AT_inline = 0x20
DW_AT_is_optional = 0x21
DW_AT_lower_bound = 0x22
DW_AT_producer = 0x25
DW_AT_prototyped = 0x27
DW_AT_return_addr = 0x2a
DW_AT_start_scope = 0x2c
DW_AT_bit_stride = 0x2e
DW_AT_upper_bound = 0x2f
DW_AT_abstract_origin = 0x31
DW_AT_accessibility = 0x32
DW_AT_address_class = 0x33
DW_AT_artificial = 0x34
DW_AT_base_types = 0x35
DW_AT_calling_convention = 0x36
DW_AT_count = 0x37
DW_AT_data_member_location = 0x38
DW_AT_decl_column = 0x39
DW_AT_decl_file = 0x3a
DW_AT_decl_line = 0x3b
DW_AT_declaration = 0x3c
DW_AT_discr_list = 0x3d
DW_AT_encoding = 0x3e
DW_AT_external = 0x3f
DW_AT_frame_base = 0x40
DW_AT_friend = 0x41
DW_AT_identifier_case = 0x42
DW_AT_macro_info = 0x43
DW_AT_namelist_item = 0x44
DW_AT_priority = 0x45
DW_AT_segment = 0x46
DW_AT_specification = 0x47
DW_AT_static_link = 0x48
DW_AT_type = 0x49
DW_AT_use_location = 0x4a
DW_AT_variable_paramter = 0x4b
DW_AT_virtuality = 0x4c
DW_AT_vtable_elem_location = 0x4d
DW_AT_allocated = 0x4e
DW_AT_associated = 0x4f
DW_AT_data_location = 0x50
DW_AT_byte_stride = 0x51
DW_AT_entry_pc = 0x52
DW_AT_use_UTF8 = 0x53
DW_AT_extension = 0x54
DW_AT_ranges = 0x55
DW_AT_trampoline = 0x56
DW_AT_call_column = 0x57
DW_AT_call_file = 0x58
DW_AT_call_line = 0x59
DW_AT_description = 0x5a
DW_AT_binary_scale = 0x5b
DW_AT_decimal_scale = 0x5c
DW_AT_small = 0x5d
DW_AT_decimal_sign = 0x5e
DW_AT_digit_count = 0x5f
DW_AT_picture_string = 0x60
DW_AT_mutable = 0x61
DW_AT_threads_scaled = 0x62
DW_AT_explicit = 0x63
DW_AT_object_pointer = 0x64
DW_AT_endianity = 0x65
DW_AT_elemental = 0x66
DW_AT_pure = 0x67
DW_AT_recursive = 0x68
DW_AT_signature = 0x69  # V4
DW_AT_main_subprogram = 0x6a  # V4
DW_AT_data_bit_offset = 0x6b  # V4
DW_AT_const_expr = 0x6c  # V4
DW_AT_enum_class = 0xd  # V4
DW_AT_linkage_name = 0x6e  # V4
# v5 only. can appear in v4 as gnu extensions
DW_AT_string_length_bit_size = 0x6f
DW_AT_string_length_byte_size = 0x70
DW_AT_rank = 0x71
DW_AT_str_offsets_base = 0x72
DW_AT_addr_base = 0x73
DW_AT_rnglists_base = 0x74
# reserved
DW_AT_dwo_name = 0x76
DW_AT_reference = 0x77
DW_AT_rvalue_reference = 0x78
DW_AT_macros = 0x79
DW_AT_call_all_calls = 0x7a
DW_AT_call_all_source_calls = 0x7b
DW_AT_call_all_tail_calls = 0x7c
DW_AT_call_return_pc = 0x7d
DW_AT_call_value = 0x7e
DW_AT_call_origin = 0x7f
DW_AT_call_parameter = 0x80
DW_AT_call_pc = 0x81
DW_AT_call_tail_call = 0x82
DW_AT_call_target = 0x83
DW_AT_call_target_clobbered = 0x84
DW_AT_call_data_location = 0x85
DW_AT_call_data_value = 0x86
DW_AT_no_return = 0x87
DW_AT_alignment = 0x88
DW_AT_export_symbols = 0x89
DW_AT_deleted = 0x8a
DW_AT_defaulted = 0x8b
DW_AT_loclists_base = 0x8c
DW_AT_lo_user = 0x2000
DW_AT_hi_user = 0x3fff


# GNU Attributes. Typically only for v4 now since a lot got mainlined in v5
DW_AT_GNU_vector = 0x2107
DW_AT_GNU_guarded_by = 0x2108
DW_AT_GNU_pt_guarded_by = 0x2109
DW_AT_GNU_guarded = 0x210a
DW_AT_GNU_pt_guarded = 0x210b
DW_AT_GNU_locks_excluded = 0x210c
DW_AT_GNU_exclusive_locks_required = 0x210d
DW_AT_GNU_shared_locks_required = 0x210e
DW_AT_GNU_odr_signature = 0x210f
DW_AT_GNU_template_name = 0x2110
DW_AT_GNU_call_site_value = 0x2111
DW_AT_GNU_call_site_data_value = 0x2112
DW_AT_GNU_call_site_target = 0x2113
DW_AT_GNU_call_site_target_clobbered = 0x2114
DW_AT_GNU_tail_call = 0x2115
DW_AT_GNU_all_tail_call_sites = 0x2116
DW_AT_GNU_all_call_sites = 0x2117
DW_AT_GNU_all_source_call_sites = 0x2118
DW_AT_GNU_macros = 0x2119
DW_AT_GNU_deleted = 0x211a
DW_AT_GNU_dwo_name = 0x2130
DW_AT_GNU_dwo_id = 0x2131
DW_AT_GNU_ranges_base = 0x2132
DW_AT_GNU_addr_base = 0x2133
DW_AT_GNU_pubnames = 0x2134
DW_AT_GNU_pubtypes = 0x2135

dwarf_attribute_names = {
    DW_AT_sibling: 'sibling',
    DW_AT_location: 'location',
    DW_AT_name: 'name',
    DW_AT_ordering: 'ordering',
    DW_AT_byte_size: 'byte_size',
    DW_AT_bit_offset: 'bit_offset',
    DW_AT_bit_size: 'bit_size',
    DW_AT_stmt_list: 'stmt_list',
    DW_AT_low_pc: 'low_pc',
    DW_AT_high_pc: 'high_pc',
    DW_AT_language: 'language',
    DW_AT_discr: 'discr',
    DW_AT_discr_value: 'discr_value',
    DW_AT_visibility: 'visibility',
    DW_AT_import: 'import',
    DW_AT_string_length: 'string_length',
    DW_AT_common_reference: 'common_reference',
    DW_AT_comp_dir: 'comp_dir',
    DW_AT_const_value: 'const_value',
    DW_AT_containing_type: 'containing_type',
    DW_AT_default_value: 'default_value',
    DW_AT_inline: 'inline',
    DW_AT_is_optional: 'is_optional',
    DW_AT_lower_bound: 'lower_bound',
    DW_AT_producer: 'producer',
    DW_AT_prototyped: 'prototyped',
    DW_AT_return_addr: 'return_addr',
    DW_AT_start_scope: 'start_scope',
    DW_AT_bit_stride: 'bit_stride',
    DW_AT_upper_bound: 'uppder_bound',
    DW_AT_abstract_origin: 'abstract_origin',
    DW_AT_accessibility: 'accessibility',
    DW_AT_address_class: 'address_class',
    DW_AT_artificial: 'artificial',
    DW_AT_base_types: 'base_types',
    DW_AT_calling_convention: 'calling_convention',
    DW_AT_count: 'count',
    DW_AT_data_member_location: 'data_member_location',
    DW_AT_decl_column: 'decl_column',
    DW_AT_decl_file: 'decl_file',
    DW_AT_decl_line: 'decl_line',
    DW_AT_declaration: 'declaration',
    DW_AT_discr_list: 'discr_list',
    DW_AT_encoding: 'encoding',
    DW_AT_external: 'external',
    DW_AT_frame_base: 'frame_base',
    DW_AT_friend: 'friend',
    DW_AT_identifier_case: 'identifier_case',
    DW_AT_macro_info: 'macro_info',
    DW_AT_namelist_item: 'namelist_item',
    DW_AT_priority: 'prority',
    DW_AT_segment: 'segment',
    DW_AT_specification: 'specification',
    DW_AT_static_link: 'static_link',
    DW_AT_type: 'type',
    DW_AT_use_location: 'use_location',
    DW_AT_variable_paramter: 'variable_parameter',
    DW_AT_virtuality: 'virtuality',
    DW_AT_vtable_elem_location: 'vtable_elem_location',
    DW_AT_allocated: 'allocated',
    DW_AT_associated: 'associated',
    DW_AT_data_location: 'data_location',
    DW_AT_byte_stride: 'byte_stride',
    DW_AT_entry_pc: 'entry_pc',
    DW_AT_use_UTF8: 'use_utf8',
    DW_AT_extension: 'extension',
    DW_AT_ranges: 'ranges',
    DW_AT_trampoline: 'trampoline',
    DW_AT_call_column: 'call_column',
    DW_AT_call_file: 'call_file',
    DW_AT_call_line: 'call_line',
    DW_AT_description: 'description',
    DW_AT_binary_scale: 'binary_scale',
    DW_AT_decimal_scale: 'decimal_scale',
    DW_AT_small: 'small',
    DW_AT_decimal_sign: 'decimal_sign',
    DW_AT_digit_count: 'digit_count',
    DW_AT_picture_string: 'picture_string',
    DW_AT_mutable: 'mutable',
    DW_AT_threads_scaled: 'threads_scaled',
    DW_AT_explicit: 'explicit',
    DW_AT_object_pointer: 'object_pointer',
    DW_AT_endianity: 'endianity',
    DW_AT_elemental: 'elemental',
    DW_AT_pure: 'pure',
    DW_AT_recursive: 'recursive',
    DW_AT_signature: 'signature',
    DW_AT_main_subprogram: 'main_subprogram',
    DW_AT_data_bit_offset: 'data_bit_offset',
    DW_AT_const_expr: 'const_expr',
    DW_AT_enum_class: 'enum_class',
    DW_AT_linkage_name: 'linkage_name',

    DW_AT_string_length_bit_size: 'string_length_bit_size',
    DW_AT_string_length_byte_size: 'string_length_byte_size',
    DW_AT_rank: 'rank',
    DW_AT_str_offsets_base: 'str_offsets_base',
    DW_AT_addr_base: 'addr_base',
    DW_AT_rnglists_base: 'rnglists_base',
    DW_AT_dwo_name: 'dwo_name',
    DW_AT_reference: 'reference',
    DW_AT_rvalue_reference: 'rvalue_reference',
    DW_AT_macros: 'macros',
    DW_AT_call_all_calls: 'call_all_calls',
    DW_AT_call_all_source_calls: 'call_all_source_calls',
    DW_AT_call_all_tail_calls: 'call_all_tail_calls',
    DW_AT_call_return_pc: 'call_return_pc',
    DW_AT_call_value: 'call_value',
    DW_AT_call_origin: 'call_origin',
    DW_AT_call_parameter: 'call_parameter',
    DW_AT_call_pc: 'call_pc',
    DW_AT_call_tail_call: 'call_tail_call',
    DW_AT_call_target: 'call_target',
    DW_AT_call_target_clobbered: 'call_target_clobbered',
    DW_AT_call_data_location: 'call_data_location',
    DW_AT_call_data_value: 'call_data_value',
    DW_AT_no_return: 'no_return',
    DW_AT_alignment: 'alignment',
    DW_AT_export_symbols: 'export_symbols',
    DW_AT_deleted: 'deleted',
    DW_AT_defaulted: 'defaulted',
    DW_AT_loclists_base: 'loclists_base',
    DW_AT_lo_user: 'lo_user',
    DW_AT_hi_user: 'hi_user',
}

gnu_attribute_names = {
    DW_AT_GNU_vector: 'vector',
    DW_AT_GNU_guarded_by: 'guarded_by',
    DW_AT_GNU_pt_guarded_by: 'pt_guarded_by',
    DW_AT_GNU_guarded: 'guarded',
    DW_AT_GNU_pt_guarded: 'pt_guarded',
    DW_AT_GNU_locks_excluded: 'locks_excluded',
    DW_AT_GNU_exclusive_locks_required: 'exclusive_locks_required',
    DW_AT_GNU_shared_locks_required: 'shared_locks_required',
    DW_AT_GNU_odr_signature: 'odr_signature',
    DW_AT_GNU_template_name: 'template_name',
    DW_AT_GNU_call_site_value: 'call_site_value',
    DW_AT_GNU_call_site_data_value: 'call_site_data_value',
    DW_AT_GNU_call_site_target: 'call_site_target',
    DW_AT_GNU_call_site_target_clobbered: 'call_site_target_clobbered',
    DW_AT_GNU_tail_call: 'tail_call',
    DW_AT_GNU_all_tail_call_sites: 'all_tail_call_sites',
    DW_AT_GNU_all_call_sites: 'all_call_sites',
    DW_AT_GNU_all_source_call_sites: 'all_source_call_sites',
    DW_AT_GNU_macros: 'macros',
    DW_AT_GNU_deleted: 'deleted',
    DW_AT_GNU_dwo_name: 'dwo_name',
    DW_AT_GNU_dwo_id: 'dwo_id',
    DW_AT_GNU_ranges_base: 'ranges_base',
    DW_AT_GNU_addr_base: 'addr_base',
    DW_AT_GNU_pubnames: 'pubnames',
    DW_AT_GNU_pubtypes: 'pubtypes',
}

# DWARF Attribute Form Encodings
DW_FORM_addr = 0x1
DW_FORM_block2 = 0x3
DW_FORM_block4 = 0x4
DW_FORM_data2 = 0x5
DW_FORM_data4 = 0x6
DW_FORM_data8 = 0x7
DW_FORM_string = 0x8
DW_FORM_block = 0x9
DW_FORM_block1 = 0xa
DW_FORM_data1 = 0xb
DW_FORM_flag = 0xc
DW_FORM_sdata = 0xd
DW_FORM_strp = 0xe
DW_FORM_udata = 0xf
DW_FORM_ref_addr = 0x10
DW_FORM_ref1 = 0x11
DW_FORM_ref2 = 0x12
DW_FORM_ref4 = 0x13
DW_FORM_ref8 = 0x14
DW_FORM_ref_udata = 0x15
DW_FORM_indirect = 0x16
DW_FORM_sec_offset = 0x17  # V4
DW_FORM_exprloc = 0x18  # V4
DW_FORM_flag_present = 0x19  # V4

DW_FORM_strx = 0x1a
DW_FORM_addrx = 0x1b
DW_FORM_ref_sup4 = 0x1c
DW_FORM_strp_sup = 0x1d
DW_FORM_data16 = 0x1e
DW_FORM_line_strp = 0x1f

DW_FORM_ref_sig8 = 0x20  # V4

DW_FORM_implicit_const = 0x21
DW_FORM_loclistx = 0x22
DW_FORM_rnglistx = 0x23
DW_FORM_ref_sup8 = 0x24
DW_FORM_strx1 = 0x25
DW_FORM_strx2 = 0x26
DW_FORM_strx3 = 0x27
DW_FORM_strx4 = 0x28
DW_FORM_addrx1 = 0x29
DW_FORM_addrx2 = 0x2a
DW_FORM_addrx3 = 0x2b
DW_FORM_addrx4 = 0x2c


DW_LANG_C89 = 0x01
DW_LANG_C = 0x02
DW_LANG_Ada83 = 0x03
DW_LANG_Cpp = 0x04
DW_LANG_Cobol74 = 0x05
DW_LANG_Cobol85 = 0x06
DW_LANG_Fortran77 = 0x07
DW_LANG_Fortran90 = 0x08
DW_LANG_Pascal83 = 0x09
DW_LANG_Modula2 = 0x0a
DW_LANG_Java = 0x0b
DW_LANG_C99 = 0x0c
DW_LANG_Ada95 = 0x0d
DW_LANG_Fortran95 = 0x0e
DW_LANG_PLI = 0x0f
DW_LANG_ObjC = 0x10
DW_LANG_ObjCpp = 0x11
DW_LANG_UPC = 0x12
DW_LANG_D = 0x13
DW_LANG_Python = 0x14
DW_LANG_lo_user = 0x8000
DW_LANG_hi_user = 0xffff

DW_ID_case_sensitive = 0x00
DW_ID_up_case = 0x01
DW_ID_down_case = 0x02
DW_ID_case_insensitive = 0x03
