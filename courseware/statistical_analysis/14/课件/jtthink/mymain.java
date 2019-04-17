package com.jtthink;

import com.alibaba.otter.canal.client.CanalConnector;
import com.alibaba.otter.canal.client.CanalConnectors;
import com.alibaba.otter.canal.protocol.CanalEntry.*;
import com.alibaba.otter.canal.protocol.Message;
import com.google.protobuf.InvalidProtocolBufferException;
import com.jtthink.data.DataUtil;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.util.HashMap;
import java.util.List;

import static java.lang.System.out;

public class mymain {

    public static void main(String[] args) throws InterruptedException, IOException {
        CanalConnector connector = CanalConnectors.newSingleConnector(
                new InetSocketAddress("192.168.29.128",
                11111), "test", "canal", "canal");
        connector.connect();
       // connector.subscribe(".*\\..*");
        connector.subscribe("employees\\.test");
        while(true){
            Message message= connector.getWithoutAck(2);
            long batchId = message.getId();
            int size = message.getEntries().size();//获取一堆数据对象
            if (batchId == -1 || size == 0) {
                Thread.sleep(1000);
            }
            else {
                List<Entry>  entries=message.getEntries();//获取一堆数据对象
                for(Entry e : entries){
                    if(e.getEntryType()==EntryType.TRANSACTIONBEGIN || e.getEntryType()==EntryType.TRANSACTIONEND) {
                        continue;
                    }
                    RowChange rowChange=null;
                    try {
                          rowChange=RowChange.parseFrom(e.getStoreValue());
                    } catch (InvalidProtocolBufferException e1) {
                        e1.printStackTrace();
                    }
                    if(rowChange.getEventType()==EventType.INSERT){
                       for(RowData rowData:rowChange.getRowDatasList()){
                           HashMap<String,Object> postData=new HashMap<String,Object>();
                           for(Column column:rowData.getAfterColumnsList()){
                               //out.println(column.getName()+":"+column.getValue()+":"+column.getMysqlType());
                               postData.put(column.getName(),column.getValue());
                           }
                          out.println(DataUtil.add(postData));

                       }


                    }

                }
                //上面假设就是业务处理成功
                 connector.ack(batchId); //假设业务处理成功了， ack消息


            }
        }

    }
}
