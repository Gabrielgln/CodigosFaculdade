/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package controller;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import model.Agendamento;
import model.Cliente;
import util.ConnectionFactory;

/**
 *
 * @author gabri
 */
public class AgendamentoController {
    
    public void save(Agendamento agendamento){
        String sql = "INSERT INTO agendamentos (barbeiroNome,servicoDescricao,dataHoraRegistro,clienteEmail) VALUES (?,?,?,?)";
        Connection conn = null;
        PreparedStatement statement = null;

        try{
            conn = ConnectionFactory.getConnection();
            statement = conn.prepareStatement(sql);
            
            statement.setString(1, agendamento.getBarbeiroNome());
            statement.setString(2, agendamento.getServicoDescricao());
            statement.setString(3, agendamento.getDataHoraRegistro());
            statement.setString(4, agendamento.getClienteEmail());
            statement.execute();

        }catch(SQLException ex){
            throw new RuntimeException("Erro ao salvar o cliente " + ex.getMessage(), ex);
        }finally{
            ConnectionFactory.closeConnection(conn, statement);
        }
    
    }

}
