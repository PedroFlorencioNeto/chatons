# ChatONS - Prova de Conceito

Este repositório apresenta o **ChatONS**, uma prova de conceito (PoC) desenvolvida a partir da ideiado desafio solicitado no **DatathONS– 6ª Edição**.  
O projeto demonstra como técnicas modernas de **Recuperação Aumentada por Geração (RAG)** e **sistemas multiagente baseados em LLMs** podem ser aplicadas para construir um mecanismo de **Perguntas e Respostas (Q&A)** sobre o **Portal de Dados Abertos do ONS**.

## 🎯 Objetivo

Validar a integração entre **LLMs, pipelines de RAG e coordenação multiagente**, oferecendo uma interface de consulta que permita ao usuário explorar os dados abertos do ONS de forma **mais acessível, contextualizada e inteligente**.  

## 🧠 Arquitetura Multiagente

A solução adota uma abordagem modular com agentes especializados que colaboram para entregar a resposta final:

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

---

## 🛠️ Stack Tecnológica

- **Python** – linguagem principal.  
- **LangChain** – orquestração das LLMs, fluxos de RAG e agentes.  
- **Qdrant Vector Store** – armazenamento vetorial para busca semântica.  
- **FastAPI** – exposição da API REST.  
- **LLM as a Judge** – validação de respostas por meio de grandes modelos de linguagem.  

## ⚙️ Fluxo de Execução

1. O usuário envia uma consulta.  
2. O **Agente de Identificação de Perfil** interpreta o contexto e adapta a interação.  
3. O **Agente de Classificação de Intenção** decide o caminho:  
   - **Dicionário de Dados** (RAG) 
   - ou **Análise/Inferência** sobre os dados operacionais do ONS.  
4. Os agentes especializados (Recuperação, Análise, Resposta) geram a resposta.  
5. A **LLM as a Judge** avalia a qualidade da resposta:  
   - Se válida → resposta entregue ao usuário.  
   - Se inconsistente → nova rodada de agentes até correção.