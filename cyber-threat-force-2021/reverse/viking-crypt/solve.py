import codecs

cleartext = b'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non enim quam. Morbi luctus tortor dolor, sed pellentesque urna vestibulum eget. In egestas diam tempus risus molestie, id consectetur ante euismod. Integer eget erat sapien.'

cipher = '85ad502b65007232f15657689af325bbccc6cb4f9ca7129f24074a1bb65bc8c30162703e3f36149f38c754567af424eb60682eda379edab1b7fe5b44c4df29c471f802c8d8716192291c829b89c3c49695ec48abf2f3721e5b229a20afb2b7c751779c51ff63f378a7a53c27113b306c26fc2b87562768cc82b70cfdbd3fc93730f890234ac890c6e6b9e052f65341eaaf3f7e56d9476c170f17dd5e3830867656c0fd885a68a55ae58bcb182a09ee0a840a03511fb3222d25637b1d344340168dfebdd97a8bc327a36e6d9703f9e6427e9dfd07df86f0140a067a3a843aeef6f4782df2f1e56e380957c2'

key = [a ^ b for a, b in zip(cleartext, codecs.decode(cipher, 'hex'))]

print(bytes([a ^ b for a, b in zip(key, codecs.decode('8a9b600b5a745d39cb7c7e7890e816848a9fe77280b42ca0751d150bb849', 'hex'))]))

