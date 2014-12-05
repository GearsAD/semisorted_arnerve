/* LCM type definition class file
 * This file was automatically generated by lcm-gen
 * DO NOT MODIFY BY HAND!!!!
 */

using System;
using System.Collections.Generic;
using System.IO;
using LCM.LCM;
 
namespace semisorted_arnerve
{
    public sealed class bot_update_t : LCM.LCM.LCMEncodable
    {
        public int timestamp;
        public String name;
        public int numBytes_cameraFrameJpeg;
        public byte[] cameraFrameJpeg;
        public float batteryPercentage;
 
        public bot_update_t()
        {
        }
 
        public static readonly ulong LCM_FINGERPRINT;
        public static readonly ulong LCM_FINGERPRINT_BASE = 0x45d643a2c5ff1d60L;
 
        static bot_update_t()
        {
            LCM_FINGERPRINT = _hashRecursive(new List<String>());
        }
 
        public static ulong _hashRecursive(List<String> classes)
        {
            if (classes.Contains("semisorted_arnerve.bot_update_t"))
                return 0L;
 
            classes.Add("semisorted_arnerve.bot_update_t");
            ulong hash = LCM_FINGERPRINT_BASE
                ;
            classes.RemoveAt(classes.Count - 1);
            return (hash<<1) + ((hash>>63)&1);
        }
 
        public void Encode(LCMDataOutputStream outs)
        {
            outs.Write((long) LCM_FINGERPRINT);
            _encodeRecursive(outs);
        }
 
        public void _encodeRecursive(LCMDataOutputStream outs)
        {
            byte[] __strbuf = null;
            outs.Write(this.timestamp); 
 
            __strbuf = System.Text.Encoding.GetEncoding("US-ASCII").GetBytes(this.name); outs.Write(__strbuf.Length+1); outs.Write(__strbuf, 0, __strbuf.Length); outs.Write((byte) 0); 
 
            outs.Write(this.numBytes_cameraFrameJpeg); 
 
            for (int a = 0; a < this.numBytes_cameraFrameJpeg; a++) {
                outs.Write(this.cameraFrameJpeg[a]); 
            }
 
            outs.Write(this.batteryPercentage); 
 
        }
 
        public bot_update_t(byte[] data) : this(new LCMDataInputStream(data))
        {
        }
 
        public bot_update_t(LCMDataInputStream ins)
        {
            if ((ulong) ins.ReadInt64() != LCM_FINGERPRINT)
                throw new System.IO.IOException("LCM Decode error: bad fingerprint");
 
            _decodeRecursive(ins);
        }
 
        public static semisorted_arnerve.bot_update_t _decodeRecursiveFactory(LCMDataInputStream ins)
        {
            semisorted_arnerve.bot_update_t o = new semisorted_arnerve.bot_update_t();
            o._decodeRecursive(ins);
            return o;
        }
 
        public void _decodeRecursive(LCMDataInputStream ins)
        {
            byte[] __strbuf = null;
            this.timestamp = ins.ReadInt32();
 
            __strbuf = new byte[ins.ReadInt32()-1]; ins.ReadFully(__strbuf); ins.ReadByte(); this.name = System.Text.Encoding.GetEncoding("US-ASCII").GetString(__strbuf);
 
            this.numBytes_cameraFrameJpeg = ins.ReadInt32();
 
            this.cameraFrameJpeg = new byte[(int) numBytes_cameraFrameJpeg];
            for (int a = 0; a < this.numBytes_cameraFrameJpeg; a++) {
                this.cameraFrameJpeg[a] = ins.ReadByte();
            }
 
            this.batteryPercentage = ins.ReadSingle();
 
        }
 
        public semisorted_arnerve.bot_update_t Copy()
        {
            semisorted_arnerve.bot_update_t outobj = new semisorted_arnerve.bot_update_t();
            outobj.timestamp = this.timestamp;
 
            outobj.name = this.name;
 
            outobj.numBytes_cameraFrameJpeg = this.numBytes_cameraFrameJpeg;
 
            outobj.cameraFrameJpeg = new byte[(int) numBytes_cameraFrameJpeg];
            for (int a = 0; a < this.numBytes_cameraFrameJpeg; a++) {
                outobj.cameraFrameJpeg[a] = this.cameraFrameJpeg[a];
            }
 
            outobj.batteryPercentage = this.batteryPercentage;
 
            return outobj;
        }
    }
}
