# 🛡️ Clique Seguro

## 💡 Sobre o Projeto - Proposta

A transição para o mundo digital — como o uso do Pix e de bancos digitais — gera desconfiança e medo de fraudes, roubos virtuais ou clonagens em pessoas idosas e indivíduos com dificuldades no uso de tecnologias móveis. Propor a criação de uma plataforma digital interativa destinada ao aprendizado prático e seguro foi uma ideia viável para resolver essa situação. Ela apoia os usuários no treinamento de suas rotinas e atividades diárias, garantindo maior previsibilidade, segurança, inclusão social e qualidade de vida. Sendo uns dos seus objetivos:

* Capacitar o público idoso a realizar tarefas do dia a dia no celular através de explicações visuais claras e sem pressa.
* Promover a autonomia e segurança de indivíduos com limitações na navegação digital através de orientações antifraude simplificadas.

---

## 📄 Funcionalidades

* **Sistema de Cadastro e Login:** Criação e configuração de contas para salvar e acompanhar o progresso das lições de onde parou.
* **Trilhas de Aprendizado por Blocos:** Conteúdos categorizados de forma limpa e divididos por temas específicos (Ferramentas do Celular, Comunicação, Golpes e Segurança).
* **Visualização Interativa e Guiada:** Lições estruturadas passo a passo com telas limpas, sem poluição visual e com foco visual redobrado.
* **Interface Hiper-Acessível:** Funcionalidades integradas para aumento de fonte (zoom), modo de alto contraste e recurso de leitura de texto na tela.

---

## 🎬 Demonstração

### Tela Inicial - Escolha de Categorias
<img width="1600" height="836" alt="Image" src="https://github.com/user-attachments/assets/5ad543b5-1b5f-4423-90ef-8399e8c550c3" />

### Interface de Lições - Passo a Passo Interativo
<img width="1600" height="880" alt="Image" src="https://github.com/user-attachments/assets/cdef19c1-5d6d-401b-bb4c-c4b397c79a48" />

---

## 💻 Tecnologias Utilizadas

| Camada | Tecnologia | Motivo |
| :--- | :--- | :--- |
| **Front-End** | HTML5, CSS3 e JavaScript | Camada de apresentação responsável pela interface do usuário através de templates responsivos. Prioriza a ergonomia e a acessibilidade (como botões grandes e alto contraste) para reduzir a carga cognitiva e adaptar-se dinamicamente ao perfil do idoso. |
| **Back-End** | Python e Django 6.0 | Linguagem principal e framework web que adotam o padrão de arquitetura MVT (Model-View-Template). Fornecem alta escalabilidade, suporte a operações assíncronas e proteções nativas contra vulnerabilidades comuns da web para suportar o processamento dinâmico do suporte adaptativo. |
| **Banco de Dados** | SQLite | Banco leve e integrado ao Django, ideal para facilitar o desenvolvimento, a portabilidade e a agilidade nas consultas. |
| **Deploy** | Render | Plataforma que automatiza o processo de publicação (CI/CD) e simplifica o gerenciamento da infraestrutura web. |

## 📁 Estrutura de Pastas

```text
📦 Clique Seguro (Django Project)
├── 📄 README.md
├── 📄 manage.py
├── 📄 db.sqlite3
├── 📂 clique_seguro (aplicação Django)
│   ├── 📄 __init__.py
│   ├── 📄 settings.py
│   ├── 📄 urls.py
│   ├── 📄 views.py
│   ├── 📄 wsgi.py
│   ├── 📄 asgi.py
│   ├── 📄 context_processors.py
│   └── 📂 __pycache__
├── 📂 main (app principal)
│   ├── 📄 __init__.py
│   ├── 📄 apps.py
│   ├── 📄 models.py
│   ├── 📄 admin.py
│   ├── 📄 tests.py
│   ├── 📂 migrations
│   └── 📂 __pycache__
├── 📂 static (arquivos estáticos)
│   ├── 📂 css
│   ├── 📂 img
│   └── 📂 js
├── 📂 templates (templates HTML)
│   ├── 📄 base.html
│   ├── 📄 navbar.html
│   ├── 📄 homepage.html
│   ├── 📄 login.html
│   ├── 📄 register.html
│   ├── 📄 user_progress.html
│   ├── 📄 category_page.html
│   ├── 📄 tutorial_page.html
│   ├── 📄 dictionary_menu.html
│   ├── 📄 dictionary_icons.html
│   ├── 📄 dictionary_words.html
│   └── 📄 dictionary_page.html
└── 📂 .git

```

A
