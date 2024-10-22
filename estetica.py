import sqlite3
class ServicoEstetica:
    def conexao(self):
        conexao = sqlite3.connect("estetica_db.db")
        consulta = conexao.cursor()
        servico = """
        CREATE TABLE IF NOT EXISTS servicos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100),
        preco VARCHAR(100),
        descricao VARCHAR(100),
        duracao VARCHAR(100)  
        );
        """
        
        consulta.execute(servico)
        return conexao
    
    def zerar_id(self):
        conexao = self.conexao()
        consulta = conexao.cursor()
        # Remove todas as entradas da tabela e redefine o AUTOINCREMENT
        consulta.execute("DELETE FROM servicos")
        consulta.execute("DELETE FROM sqlite_sequence WHERE name = 'servicos'")  # Reseta a sequência do ID
        conexao.commit()
        print("IDs zerados com sucesso.")
        conexao.close()
    
    def inserir(self, nome, preco, descricao, duracao):
        conexao = self.conexao()#estamos chamando o métodp que irá conectar ao banco, esse método foi criado mais acima
        
        sql = "INSERT INTO servicos VALUES (?,?,?,?,?)"
        
        campos = (None, nome, preco, descricao, duracao)
        
        consulta = conexao.cursor()
        consulta.execute(sql, campos)
        
        conexao.commit()
        
        print(consulta.rowcount, "Linha(s) inserida(s) com sucesso")
        
        conexao.close()
    
    def consultar(self):
        conexao = self.conexao()
        consulta = conexao.cursor()
        
        sql = "SELECT * FROM servicos"
        consulta.execute(sql)
        
        resultado = consulta.fetchall()
        
        for itens in resultado:
            print(f"id: {itens[0]}")
            print(f"Nome: {itens[1]}")
            print(f"Preço: {itens[2]}")
            print(f"Descrição: {itens[3]}")
            print(f"Duração: {itens[4]}")
            print("-"*40)#Criando um separador entre os registro
            
        conexao.close()

    def deletar(self, id):
        conexao = self.conexao()
        consulta = conexao.cursor()


        sql = "DELETE FROM servicos WHERE id = ?"

        campos = (id,)# é preciso colocar uma vírgula depois do item para configurar que temos uma tupla,caso contrário não será aceito como uma tupla válida.

        consulta.execute(sql, campos)

        conexao.commit()

        print(consulta.rowcount, "linha(s) deletada(s) com sucesso")

        conexao.close()

    def atualizar(self, nome, id):
        conexao = self.conexao()
        consulta = conexao.cursor()

        sql = "UPDATE servicos SET nome = ? WHERE id = ?"

        campos = (nome, id)

        consulta.execute(sql, campos)

        conexao.commit()

        print(consulta.rowcount, "Linha(S) atualizada(s) com sucesso")

        conexao.close()

    def consultarServicoIndividual(self, id):
        conexao = self.conexao()  # Utiliza o método de conexão existente
        consulta = conexao.cursor()
        
        # Consulta SQL para obter um serviço específico pelo ID
        consulta.execute("SELECT * FROM servicos WHERE id = ?", (id,))
        servico = consulta.fetchone()  # Pega apenas o primeiro resultado
        
        # Verificar se o serviço foi encontrado
        if servico:
            print(f"ID: {servico[0]}, Nome: {servico[1]}, Preço: {servico[2]}, Descrição: {servico[3]}, Duração: {servico[4]} minutos")
        else:
            print("Erro: Serviço não encontrado.")
        
        conexao.close() 