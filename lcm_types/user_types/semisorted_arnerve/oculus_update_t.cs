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
    public sealed class oculus_update_t : LCM.LCM.LCMEncodable
    {
        public long timestamp;
        public double[] headorientation;
        public double[] headposition;
 
        public oculus_update_t()
        {
            headorientation = new double[3];
            headposition = new double[3];
        }
 
        public static readonly ulong LCM_FINGERPRINT;
        public static readonly ulong LCM_FINGERPRINT_BASE = 0x2168a8d99c85d900L;
 
        static oculus_update_t()
        {
            LCM_FINGERPRINT = _hashRecursive(new List<String>());
        }
 
        public static ulong _hashRecursive(List<String> classes)
        {
            if (classes.Contains("semisorted_arnerve.oculus_update_t"))
                return 0L;
 
            classes.Add("semisorted_arnerve.oculus_update_t");
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
            outs.Write(this.timestamp); 
 
            for (int a = 0; a < 3; a++) {
                outs.Write(this.headorientation[a]); 
            }
 
            for (int a = 0; a < 3; a++) {
                outs.Write(this.headposition[a]); 
            }
 
        }
 
        public oculus_update_t(byte[] data) : this(new LCMDataInputStream(data))
        {
        }
 
        public oculus_update_t(LCMDataInputStream ins)
        {
            if ((ulong) ins.ReadInt64() != LCM_FINGERPRINT)
                throw new System.IO.IOException("LCM Decode error: bad fingerprint");
 
            _decodeRecursive(ins);
        }
 
        public static semisorted_arnerve.oculus_update_t _decodeRecursiveFactory(LCMDataInputStream ins)
        {
            semisorted_arnerve.oculus_update_t o = new semisorted_arnerve.oculus_update_t();
            o._decodeRecursive(ins);
            return o;
        }
 
        public void _decodeRecursive(LCMDataInputStream ins)
        {
            this.timestamp = ins.ReadInt64();
 
            this.headorientation = new double[(int) 3];
            for (int a = 0; a < 3; a++) {
                this.headorientation[a] = ins.ReadDouble();
            }
 
            this.headposition = new double[(int) 3];
            for (int a = 0; a < 3; a++) {
                this.headposition[a] = ins.ReadDouble();
            }
 
        }
 
        public semisorted_arnerve.oculus_update_t Copy()
        {
            semisorted_arnerve.oculus_update_t outobj = new semisorted_arnerve.oculus_update_t();
            outobj.timestamp = this.timestamp;
 
            outobj.headorientation = new double[(int) 3];
            for (int a = 0; a < 3; a++) {
                outobj.headorientation[a] = this.headorientation[a];
            }
 
            outobj.headposition = new double[(int) 3];
            for (int a = 0; a < 3; a++) {
                outobj.headposition[a] = this.headposition[a];
            }
 
            return outobj;
        }
    }
}

