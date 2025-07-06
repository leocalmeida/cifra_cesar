# 🔒 A Cifra de César
A Cifra de César é uma das formas mais simples e conhecidas de cifragem por substituição. Seu nome é uma homenagem a Júlio César, que a utilizava para proteger suas comunicações militares.

## ⚙️ Como funciona?
O princípio da Cifra de César é remarkably straightforward: cada letra do texto original (chamado de texto plano ou texto claro) é substituída por outra letra que se encontra um número fixo de posições adiante no alfabeto. Esse número fixo de posições é a chave da cifra.

Exemplo:
```
Imagine que a chave seja 3.
Se a letra original for 'A', ela é substituída por 'D' (A + 3 posições).
Se a letra original for 'B', ela é substituída por 'E' (B + 3 posições).
E assim por diante.
```

Quando se atinge o final do alfabeto (a letra 'Z'), a contagem recomeça do início. Por exemplo, com uma chave de 3, a letra 'X' seria substituída por 'A', 'Y' por 'B' e 'Z' por 'C'.

## ✉️ Cifragem e Decifragem
### Cifragem: 
Para criptografar uma mensagem, você aplica o deslocamento da chave a cada letra do texto plano.

### Decifragem: 
Para decifrar uma mensagem cifrada, basta aplicar o deslocamento inverso da chave. Ou seja, se a chave de cifragem foi "+3", a chave de decifragem será "-3".

### Segurança
Apesar de sua simplicidade e importância histórica, a Cifra de César é considerada extremamente frágil em termos de segurança nos dias de hoje. Existem apenas 25 chaves possíveis (já que um deslocamento de 26 seria o mesmo que nenhum deslocamento). Isso significa que uma mensagem cifrada com a Cifra de César pode ser facilmente quebrada usando um ataque de força bruta, onde todas as 25 chaves são testadas até que o texto claro seja revelado.

### Relevância
Mesmo não sendo segura para comunicações modernas, a Cifra de César é frequentemente utilizada como um exemplo introdutório no estudo da criptografia devido à sua clareza conceitual. Ela serve como base para entender conceitos mais complexos de substituição e como a escolha da chave e a complexidade do algoritmo impactam a segurança de uma mensagem.

---
[Leonardo C. A.](https://www.linkedin.com/in/almeidaleoc/)
