class CipherBase:

    def __init__(self, encrypt_message):
        self.allow_letters = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz'
        self.freq = 'TEOAISRHNUCMDLGWFPYKJBVQX'
        self.freq_encrypt = ''
        self.encrypt_message = encrypt_message
        self.decrypt_message = ''
        self.__decrypt()

    def __decrypt(self):
        # CONTAR y AGRUPAR cada letra del mensaje
        letters = {}
        for letter in self.encrypt_message:
            if letter in self.allow_letters:
                if letter.upper() in letters:
                    letters[letter.upper()] += 1
                else:
                    letters[letter.upper()] = 1
        
        # ORDENAR DESCENDENTE
        letters = dict(sorted(letters.items(), key=lambda l: l[1], reverse=True))
        
        # CONCATENAR LETRAS
        self.freq_encrypt = ''.join(k for k in letters.keys())

        self.decrypt_message = ''
        for letter in self.encrypt_message:
            p = self.freq_encrypt.find(letter.upper())
            decrypted_letter = self.freq[p]
            if ( p > -1 ):
                if letter.isupper():
                    self.decrypt_message += decrypted_letter.upper()
                else:
                    self.decrypt_message += decrypted_letter.lower()
            else:
                self.decrypt_message += letter

    def print_decrypt_message(self):
        # Recuerda mantener mayúsculas, espacios y saltos de línea.
        return self.decrypt_message

    def __str__(self):
        return self.print_decrypt_message()


class Cipher(CipherBase):
    def __init__(self, message):
        super().__init__(message)


encrypt_message = '''
Bgc-bfufb tegaedppqna ql aggv zge xof tegaedppfe'l lgjb.
Xof adpf vflqanfe logjbvn'x hf pdwqna d cgebv qn coqro xof tbdkfe ql
mjlx d lpdbb tdex.
Xof tbdkfe QL XOF HGLL; qx'l kgje vjxk xg fnxfexdqn oqp ge ofe.
Zgrjl ql d pdxxfe gz vfrqvqna codx xoqnal kgj def ngx agqna xg vg.
Xof rglx gz dvvqna d zfdxjef qln'x mjlx xof xqpf qx xdwfl xg rgvf qx.
Xof rglx dblg qnrbjvfl xof dvvqxqgn gz dn ghlxdrbf xg zjxjef fstdnlqgn.
Xof xeqrw ql xg tqrw xof zfdxjefl xodx vgn'x zqaox fdro gxofe.
- Mgon Rdepdrw.

(ccc.adpdljxed.rgp/uqfc/nfcl/234346?utkjpvbjr)

(ccc.hedqnkijgxf.rgp/ijgxfl/djxogel/m/mgon_rdepdrw.oxpb)
'''
cipher = Cipher(encrypt_message)
print(cipher)
