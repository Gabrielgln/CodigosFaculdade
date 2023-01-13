/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package controller;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import model.Barbeiro;
import model.Cliente;
import util.ConnectionFactory;

/**
 *
 * @author gabri
 */
public class BarbeiroController {
    
    public void save(Barbeiro barbeiro){
        
        String sql = "INSERT INTO barbeiros (nome) VALUES (?)";
        Connection conn = null;
        PreparedStatement statement = null;

        try{
            conn = ConnectionFactory.getConnection();
            statement = conn.prepareStatement(sql);
            
            statement.setString(1, barbeiro.getNome());
            statement.execute();

        }catch(SQLException ex){
            throw new RuntimeException("Erro ao salvar o barbeiro " + ex.getMessage(), ex);
        }finally{
            ConnectionFactory.closeConnection(conn, statement);
        }
    
    }
}
