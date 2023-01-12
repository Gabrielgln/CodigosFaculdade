class Mario implements IMario{
  private String estado = "pequeno";
  private int pontos = 0;

  public void PegarCogumelo(){
    if (this.estado == "pequeno"){
      this.estado = "Mario Grande";
    } 
    if(this.estado == "grande"){
      this.pontos += 1000;  
    }
    if (this.estado == "fogo"){
      this.pontos += 1000; 
    }
    if (this.estado =="capa"){
      this.pontos += 1000; 
    }  
  }

  public void PegarFlor(){
    if (this.estado == "pequeno"){
      this.estado = "M grande e Mario fogo";
    } 
    if(this.estado == "grande"){
      this.estado = "Mario fogo";  
    }
    if (this.estado  == "fogo"){
      this.pontos += 1000;
    }
    if (this.estado =="capa"){
      this.estado += "Mario fogo";
    }
  }
  
  public void PegarPena(){
    if (this.estado == "pequeno"){
      this.estado = "Mario grande e Mario capa";
    } 
    if(this.estado == "grande"){
      this.estado = "Mario capa";  
    }
    if (this.estado  == "fogo"){
      this.estado = "Mario capa";
    }
    if (this.estado =="capa"){
      this.pontos += 1000;
    } 
  }
      
  public void LevarDano(){
    if (this.estado == "pequeno"){
      this.estado = "Mario morto";
    } 
    if(this.estado == "grande"){
      this.estado = "Mario pequeno";  
    }
    if (this.estado  == "fogo"){
      this.estado = "Mario grande";  
    }
    if (this.estado == "capa"){
      this.estado = "Mario grande";  
    }
  }


  public void imprime(){
    System.out.println("Estado: "  +this.estado + "\nPontos: " + this.pontos);
  }




  
}