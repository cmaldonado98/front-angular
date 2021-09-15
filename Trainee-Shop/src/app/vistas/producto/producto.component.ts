import { Component } from '@angular/core';
import { ProductoService } from '../../servicios/api/api-productos.service';
import {MatDialogModule, MatDialogConfig, MatDialogRef, MatDialog} from '@angular/material/dialog'; 
import { Router } from '@angular/router';
@Component({
  selector: 'app-producto',
  templateUrl: './producto.component.html',
  styleUrls: ['./producto.component.css']
})
export class ProductoComponent {
  title = 'frontangular';
  tasks:any;
  supermercado:Array<any>=[];
  total:Array<any>=[];
  totalfinal:number=0;
  pvp:number=0;
  acu:number=0;
  res:number=0;
  sup_recibido:string="";
  confirmar: boolean=true;
  constructor(
    private taskService:ProductoService,private router: Router
  )  {
    this.getAllTasks();
  }
  getAllTasks(){
    this.taskService.getAllTasks().subscribe(tasks => {
      this.tasks=tasks;
      this.sup_recibido = String(sessionStorage.getItem("id"));
      let firstName = sessionStorage.getItem("id");
      console.log(`Hola, mi nombre es ${firstName}`)
      console.log('recibir',firstName);
      Object.keys(this.tasks).forEach(key => {
        if (String(this.tasks[key].Supermercado_idSupermercado) == firstName) {    
            this.supermercado.push({
              ...this.tasks[key]
            });
        }
    });
    console.log("Listado de los supermercado que son iguales a 3",this.supermercado);
    });
  }
  addProduct(idProducto: any,index: any){
      console.log([idProducto,index]);
      let cantidad:number = parseInt((<HTMLInputElement>document.getElementById(`cantidad${index}`)).value);
      let indproducto:any = Object.keys(this.tasks).find(x => this.tasks[x].idProducto == idProducto);
      let subtotal=cantidad*this.tasks[indproducto].precio;
      console.log([cantidad]);
      console.log(this.tasks[indproducto]);
      console.log(typeof this.tasks);
      if(this.tasks[indproducto].stock){
        if((cantidad>0) && (cantidad <= parseInt(this.tasks[indproducto].stock)) ){
          this.res=parseInt(this.tasks[indproducto].stock);
          console.log('esto tiene el res',this.res);
          this.res=this.res-cantidad;
          console.log('esto tiene el res 2',this.res);
        //cantidad=this.res; 
          if(this.res==0){
            alert("No existe el stock solicitado !!!");
          }
         else{
          this.total.push({
            "id":this.tasks[indproducto].idProducto,
            "nombre":this.tasks[indproducto].nombre_producto,
            "unidad":this.tasks[indproducto].unidad,
            "precio":this.tasks[indproducto].precio,
            "cantidad":cantidad,  
            "subtotal":subtotal
          }); 
          this.ftotal();
         }
        }else{
          alert("Error al ingresar los productos !!!");
        }
      }
  }  
  remProduct(id:any){
    this.total.splice(id, 1);
    console.log('mostrar',this.total);
    this.ftotal();
  }
  ftotal(){
      this.totalfinal=0;
      this.total.forEach(pro => {   
        this.totalfinal += pro.subtotal;
  }); 
  }
  ngOnInit(): void{
  }
  enviarprecio() {
    console.log("el total final", this.totalfinal);
        let idS: string = "" + this.totalfinal;
        sessionStorage.setItem("tpvp", idS);
        console.log("convertido a string es: " + idS)
        this.router.navigate(['supermercados']);
    }

    irpagos(){
      this.router.navigate(['/pago']);
      let idS: string = "" + this.totalfinal;
      sessionStorage.setItem("tpvp", idS);
      console.log("convertido a string es: " + idS)
    }
    gopagos(){
  
      
      let fac = {
  
      "cantidad": "",
      "valor": "",
      "producto_idproducto": "",
      "factura_idfactura": "",
      "iddetalle":"",
      }
      let cantidadf =  String(sessionStorage.getItem("cantf"));
      console.log(`cantidafactura ${cantidadf}`)
      
    }
  }
