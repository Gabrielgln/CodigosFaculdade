    /*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package controller;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import model.Cliente;
import model.DataHora;
import util.ConnectionFactory;

/**
 *
 * @author gabri
 */
public class DataHoraController {
    public void save(DataHora dataHora){
        String sql = "INSERT INTO datahoras (registro) VALUES (?)";
        Connection conn = null;
        PreparedStatement statement = null;

        try{
            conn = ConnectionFactory.getConnection();
            statement = conn.prepareStatement(sql);
            
            statement.setString(1, dataHora.getRegistro());
            statement.execute();

        }catch(SQLException ex){
            throw new RuntimeException("Erro ao salvar o cliente " + ex.getMessage(), ex);
        }finally{
            ConnectionFactory.closeConnection(conn, statement);
        }
    
    }
}
