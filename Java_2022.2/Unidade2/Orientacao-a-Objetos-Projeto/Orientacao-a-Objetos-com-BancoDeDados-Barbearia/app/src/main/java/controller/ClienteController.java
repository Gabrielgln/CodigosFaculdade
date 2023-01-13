package controller;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import model.Cliente;
import util.ConnectionFactory;

/**
 *
 * @author gabri
 */
public class ClienteController {
    
    public void save(Cliente cliente){
        String sql = "INSERT INTO clientes (nome,email,telefone) VALUES (?,?,?)";
        Connection conn = null;
        PreparedStatement statement = null;

        try{
            conn = ConnectionFactory.getConnection();
            statement = conn.prepareStatement(sql);
            
            statement.setString(1, cliente.getNome());
            statement.setString(2, cliente.getEmail());
            statement.setString(3, cliente.getTelefone());
            statement.execute();

        }catch(SQLException ex){
            throw new RuntimeException("Erro ao salvar o cliente " + ex.getMessage(), ex);
        }finally{
            ConnectionFactory.closeConnection(conn, statement);
        }
    
    }
    
}
