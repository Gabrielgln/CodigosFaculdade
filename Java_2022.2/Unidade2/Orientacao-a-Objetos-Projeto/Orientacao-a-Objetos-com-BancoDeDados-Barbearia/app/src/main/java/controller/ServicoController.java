/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package controller;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import model.Cliente;
import model.Servico;
import util.ConnectionFactory;

/**
 *
 * @author gabri
 */
public class ServicoController {
    
    public void save(Servico servico){
        String sql = "INSERT INTO servicos (descricao) VALUES (?)";
        
        Connection conn = null;
        PreparedStatement statement = null;

        try{
            conn = ConnectionFactory.getConnection();
            statement = conn.prepareStatement(sql);
            
            statement.setString(1, servico.getDescricao());
            statement.execute();

        }catch(SQLException ex){
            throw new RuntimeException("Erro ao salvar o servico " + ex.getMessage(), ex);
        }finally{
            ConnectionFactory.closeConnection(conn, statement);
        }
    
    }
}
