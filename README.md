# NutroMed — site institucional

Site da **NutroMed | Clínica de Emagrecimento e Estética em Salvador**, desenvolvido com prioridade para navegação no celular e contato pelo WhatsApp.

- **Repositório:** https://github.com/FelipeArauj0/nutromed
- **Versão de revisão criada com Sites:** https://nutromed-salvador.janinegabriela76.chatgpt.site
- **Proposta para análise comercial:** [proposta.md](proposta.md)

A versão hospedada em Sites possui acesso controlado. O link acima não deve ser tratado como um domínio público da clínica. Este repositório é uma cópia independente do site; commits no GitHub não atualizam automaticamente a publicação de Sites.

## Tecnologias e arquitetura

HTML5, CSS3 e JavaScript nativo, sem framework, bibliotecas de interface ou dependências de execução. O projeto é estático, de uma página, e não precisa de compilação.

O arquivo `dist/index.html` contém a marcação, os estilos em `<style>` e as interações em `<script>`. A escolha mantém a implantação simples e concentra os ajustes em um único arquivo.

## Estrutura

| Caminho | Finalidade |
| --- | --- |
| `dist/index.html` | Página completa e código das interações |
| `dist/assets/dr-marcel-portrait.jpg` | Retrato usado na abertura |
| `dist/assets/dr-marcel.jpg` | Imagem original preservada para manutenção |
| `README.md` | Documentação de desenvolvimento |
| `proposta.md` | Escopo comercial, análise da experiência e plano de mensuração |
| `vercel.json` | Publicação dos arquivos de `dist`, sem build |
| `scripts/verify.py` | Verificação de estrutura, imagens, âncoras e sintaxe JavaScript |
| `.gitignore` | Exclusões de arquivos locais e informações de ambiente |

Na seção do médico, a foto está incorporada ao HTML como uma URL `data:image/jpeg;base64,...`. Isso elimina uma requisição externa para essa imagem. O arquivo original fica em `dist/assets/dr-marcel.jpg`; modificá-lo sozinho **não** altera a foto incorporada.

A pasta e os identificadores internos de hospedagem do Sites não fazem parte desta exportação.

## Funcionalidades implementadas

- Apresentação da clínica, endereço e responsável técnico informado: Dr. Marcel Figueiredo Fontes, CREMEB 26740.
- Navegação responsiva; menu recolhido em telas de até 700 px.
- Abas de emagrecimento, estética facial e estética corporal.
- Mensagens de WhatsApp com o assunto correspondente ao serviço escolhido.
- Seletor de assunto para iniciar uma conversa com a equipe.
- Botão de WhatsApp fixo na parte inferior do celular.
- Link para localização no Google Maps, telefone e Instagram.
- Nota e quantidade de avaliações como fotografia do registro fornecido, com aviso da data.
- Perguntas frequentes com abertura e fechamento nativos (`details`/`summary`).
- Título e descrição da página, idioma pt-BR, textos alternativos, foco visível e suporte a preferência por movimento reduzido.
- Abas com navegação por teclado: setas, Home e End. O menu fecha com Escape.

O botão de WhatsApp abre uma conversa; não confirma consulta, não envia a mensagem automaticamente e não registra que houve atendimento.

## O que ainda não está implementado

- Google Analytics, Google Tag Manager, pixels ou registro próprio de eventos.
- Captura ou persistência de UTM e origem dos contatos.
- CRM, cadastro de pacientes, formulário de leads ou banco de dados.
- Agenda, confirmação automática, pagamentos ou integração com WhatsApp Business API.
- Painel administrativo, dashboard de indicadores ou relatórios automáticos.
- Busca de avaliações atualizadas ou publicação de avaliações pelo site.
- Domínio próprio e uma política de privacidade aprovada pela clínica.

Essas possibilidades estão descritas como **escopo proposto** em `proposta.md`. Não há dados históricos de visitantes ou clientes disponíveis neste projeto. O seletor de assunto funciona no navegador, sem salvar registros.

## Rodar localmente

Na raiz do repositório:

```bash
python3 -m http.server 8000 --directory dist
```

No Windows, se necessário:

```powershell
py -m http.server 8000 --directory dist
```

Abra `http://localhost:8000`. O servidor local disponibiliza apenas a pasta pública `dist`.

## Verificar o projeto

Requisitos: Python 3 e Node.js. Não é necessário instalar pacotes.

```bash
python3 scripts/verify.py
```

O verificador confere os arquivos das imagens, a imagem incorporada, identificadores únicos, destinos das âncoras, estrutura das abas e sintaxe dos scripts com `node --check`. Ele não substitui testes visuais em dispositivos, testes de contraste ou uma auditoria de acessibilidade.

Antes de uma publicação destinada ao cliente, revisar em telas de 320, 375, 639 e 1280 px, e com ampliação de texto:

- menu, alternância das três abas e perguntas frequentes;
- ausência de rolagem horizontal e textos legíveis;
- foto do médico sem distorção;
- botão fixo sem cobrir o final da página;
- mensagens, número e links de WhatsApp, telefone, Instagram e Maps.

## Editar conteúdo e contato

Este projeto **não possui `config.js`**. Edite diretamente `dist/index.html`.

| O que alterar | Onde localizar |
| --- | --- |
| Abertura e mensagem principal | `id="hero-title"` e `.hero-copy` |
| Serviços e descrições | `id="cuidados"`, `panel-saude`, `panel-facial`, `panel-corporal` |
| Apresentação do médico | `id="doutor"` |
| Perguntas frequentes | `id="duvidas"` |
| Endereço e atendimento | `id="clinica"` e `<footer>` |
| Cores e aparência | variáveis em `:root` e regras do `<style>` |
| Assuntos enviados ao WhatsApp | `data-topic`, opções de `#interest` e função `whatsapp(topic)` |
| Título e descrição para busca | `<title>` e `<meta name="description">` |

**Trocar o número:** substitua todas as ocorrências de `5571994155478`, incluindo links `wa.me`, `tel:` e a função JavaScript. Atualize também o número visível `(71) 99415-5478`. O formato de `wa.me` usa código de país, DDD e número, sem espaços ou sinais.

**Trocar a imagem da abertura:** substitua `dist/assets/dr-marcel-portrait.jpg`, mantendo o nome, ou atualize o `src` e os atributos `width`/`height`. Use foto com autorização e preserve a proporção no CSS.

**Trocar a imagem incorporada do médico:** escolha uma destas opções:

1. Substituir o `src="data:image/jpeg;base64,..."` por `src="assets/dr-marcel.jpg"` e trocar o arquivo correspondente. Isso volta a usar uma imagem externa local.
2. Gerar Base64 da nova imagem e substituir somente o conteúdo do atributo `src`, mantendo o prefixo `data:image/jpeg;base64,`.

Preserve `height:auto` na regra `.about-photo img`. Não fixe a altura de uma imagem cuja largura diminui no celular. Se mudar a proporção da foto, atualize também `aspect-ratio`, `width` e `height`.

**Atualizar avaliações:** altere a nota, a quantidade e a data em todos os pontos relacionados. O site não consulta o Google automaticamente; mantenha o aviso de que é um registro datado.

## Publicar a exportação

### Vercel

Importe `FelipeArauj0/nutromed`. O `vercel.json` define:

- framework: nenhum;
- build: nenhum;
- diretório de saída: `dist`;
- raiz do projeto: raiz do repositório.

Não configure a saída como `public` nem espere um `npm run build`: esses caminhos e comandos não existem neste projeto. Confirme que configurações manuais do painel não contradizem o arquivo. A publicação pelo Vercel é separada da versão de Sites e requer importar o repositório na conta escolhida.

### Outro serviço estático

Publique **o conteúdo de `dist`**, mantendo `index.html` na raiz pública e a pasta `assets` ao lado. Não publique a raiz inteira do repositório; a proposta e a documentação não pertencem à página da clínica.

## Dados e manutenção

O site não armazena informações em banco de dados ou `localStorage`, nem contém código próprio de analytics. Links externos levam a serviços com seus próprios tratamentos de dados.

Antes de adicionar mensuração, seguir o plano de privacidade e as separações entre analytics e atendimento em `proposta.md`. Não incluir dados de pacientes, contatos privados, credenciais ou prontuários no GitHub, URLs, eventos ou exemplos de teste.

A clínica deve validar textos, serviços disponíveis, imagens autorizadas, identidade e registro do responsável técnico antes da divulgação final. A versão de revisão contém apenas o registro profissional fornecido; não declara especialidades ou RQE que não foram comprovados.

## Histórico desta exportação

- Exportação em 8 de outubro de 2026.
- Base: versão revisada após a correção de proporção e carregamento da foto do médico.
- Commit de origem do Sites: `31032d66556421d6c9e094f5c696abe495139a4f`.
- Documentação comercial e técnica acrescentada para esta entrega no GitHub.
- Não foi realizada nova publicação de Sites nem integração de mensuração nesta exportação.
