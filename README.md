# ChatONS - Prova de Conceito

Este repositório apresenta o **ChatONS**, uma prova de conceito (PoC) desenvolvida a partir do desafio solicitado pelo Operador Nacional do Sistema Elétrico (ONS) no [**DatathONS– 6ª Edição**](https://datathons6aedicao.liga.ventures/) .  
O projeto é fruto do meu estudo de **Recuperação Aumentada por Geração (RAG)** no curso "[Building RAG Agents with LLMs](https://www.nvidia.com/pt-br/training/instructor-led-workshops/building-rag-agents-with-llms/)" da NVIDIA Deep Learning Institute com o objetivo de construir um mecanismo de **Perguntas e Respostas (Q&A)** sobre o **Portal de Dados Abertos do ONS**.

## 🎯 Objetivo

Validar a integração entre o modelo DeepSeek atribuindo contexto por meio de documentos em formato PDF de dicionários de dados, oferecendo uma interface de consulta que permita ao usuário explorar os dados abertos do ONS de forma **mais acessível, contextualizada e inteligente**.  

## 🛠️ Stack Tecnológica

- **Python** – linguagem principal.  
- **LangChain** – orquestração das LLMs, fluxos de RAG e agentes.  
- **Qdrant Vector Store** – armazenamento vetorial para busca semântica.  

## ⚙️ Próximos Passos

### 🧠 Arquitetura Multiagente

A solução adotará uma abordagem modular com agentes especializados que colaboram para entregar a resposta final:

1. **Agente de Identificação de Perfil do Usuário**  
   - Analisa a interação inicial para identificar o perfil e nível de conhecimento do usuário (ex.: técnico, gestor, público geral).  
   - Ajusta o tom e a profundidade da resposta.  

2. **Agente de Classificação de Intenção**  
   - Verifica se a entrada do usuário é uma **pergunta válida**.  
   - Decide se a consulta deve:  
     - **Consultar o Dicionário de Dados** (quando a dúvida é sobre significado, definição ou metadado dos conjuntos do portal).  
     - **Executar uma Análise/Inferência** (quando a pergunta envolve cálculo, síntese de informação ou interpretação).  

3. **Agente de Recuperação**  
   - Realiza a busca semântica no **Qdrant Vector Store** para trazer informações relevantes.  

4. **Agente de Análise**  
   - Processa os dados recuperados, organiza e interpreta.  

5. **Agente de Resposta**  
   - Sintetiza a resposta final em linguagem natural, adaptada ao perfil identificado.  

6. **LLM as a Judge** 🏛️  
   - Atua como juiz das respostas geradas pelos agentes.  
   - Avalia **coerência, completude e adequação ao perfil do usuário**.  
   - Pode:  
     - Validar a resposta e entregá-la ao usuário.  
     - Solicitar uma nova tentativa de resposta caso detecte inconsistências.  
